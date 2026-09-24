#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Standalone extractor of PARSEC E11_Concept instances from an ontology (TTL).

Reads a PARSEC ontology file and produces:
  - concepts_for_metadata.json  (full metadata per concept)
  - <CONCEPTS>.tsv              (tabular view: Concept, Description, Synonyms, Category, Characterizations)
  - category_pertains.tsv       (category -> allowed celestial-body types)
  - characterizations.json      (concept -> list of characterizations)

Usage examples
--------------
# Minimal (uses defaults: ./Ontology/PARSEC_model_v.7.5.ttl, output under ./data/concepts/)
python extract_concepts_standalone.py

# Custom paths
python extract_concepts_standalone.py \
    --ontology ./Ontology/PARSEC_model_v.7.5.ttl \
    --out-dir  ./data/concepts \
    --concepts-name concepts

# Optional config file (same key=value format as parsec.config)
python extract_concepts_standalone.py --config parsec.config
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import urllib.parse
from pathlib import Path
from typing import Any, Dict, List, Optional

import rdflib
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef


# ---------------------------------------------------------------------------
# Namespaces & predicates
# ---------------------------------------------------------------------------
BASE_IRI = "https://isl.ics.forth.gr/PARSEC#"
PARSEC = Namespace(BASE_IRI)

E11 = PARSEC["E11_Concept"]
E22 = PARSEC["E22_Category"]

P48 = PARSEC["P48_belongs_in_measurement_category"]
P53 = PARSEC["P53_has_synonym"]
P54 = PARSEC["P54_has_scientific_description"]
P55 = PARSEC["P55_has_LLM_description"]
P65 = PARSEC["P65_has_lower_value_limit"]
P66 = PARSEC["P66_has_upper_value_limit"]

# FIX: real ontology property name is P68_not_allowed_in_auxiliary_category,
# NOT P68_not_allowed_in_metadata_category.
P68 = PARSEC["P68_not_allowed_in_auxiliary_category"]

P70 = PARSEC["P70_is_auxiliary"]
P72 = PARSEC["P72_category_pertains_to"]
P75 = PARSEC["P75_has_possible_characterization"]
P76 = PARSEC["P76_characterization_literal_value"]
P77 = PARSEC["P77_characterization_LLM_description"]
P86 = PARSEC["P86_follows_base_concept_units"]


# ---------------------------------------------------------------------------
# Config / args
# ---------------------------------------------------------------------------
def load_config_file(path: str) -> Dict[str, str]:
    """Parse a simple key=value config file (PARSEC style)."""
    config: Dict[str, str] = {}
    with open(path, encoding="utf8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError(f"Invalid config line: {raw!r}")
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract PARSEC E11_Concept instances into JSON/TSV/CSV."
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Optional parsec.config file (key=value). CLI args override it.",
    )
    parser.add_argument(
        "--ontology",
        default=None,
        help="Path to the PARSEC ontology TTL file.",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Directory where output files will be written.",
    )
    parser.add_argument(
        "--concepts-name",
        default=None,
        help="Base name for the TSV output (without extension).",
    )
    parser.add_argument(
        "--default-ontology",
        default=os.path.join("Ontology", "PARSEC_model_v.7.5.ttl"),
        help="Fallback ontology path if neither --ontology nor --config is provided.",
    )
    parser.add_argument(
        "--default-out-dir",
        default=os.path.join("data", "concepts"),
        help="Fallback output directory.",
    )
    parser.add_argument(
        "--default-concepts-name",
        default="concepts",
        help="Fallback concepts name (without extension).",
    )
    return parser.parse_args()


def resolve_paths(args: argparse.Namespace) -> Dict[str, Path]:
    """Merge CLI args + optional config into concrete paths."""
    cfg: Dict[str, str] = {}
    if args.config and os.path.isfile(args.config):
        cfg = load_config_file(args.config)

    ontology = (
        args.ontology
        or cfg.get("ONTOLOGY_FILE")
        or args.default_ontology
    )
    # If ontology came from config and is a bare filename, prefer ./Ontology/<name>
    ontology_path = Path(ontology)
    if not ontology_path.is_absolute() and not ontology_path.exists():
        fallback = Path("Ontology") / ontology
        if fallback.exists():
            ontology_path = fallback

    out_dir = Path(args.out_dir or args.default_out_dir)
    concepts_name = args.concepts_name or cfg.get("CONCEPTS") or args.default_concepts_name

    return {
        "ontology": ontology_path,
        "out_dir": out_dir,
        "concepts_name": Path(concepts_name).stem,  # strip .tsv/.json if provided
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def local_name(iri: Any) -> str:
    """Return the decoded local fragment of an IRI."""
    s = str(iri)
    if "#" in s:
        s = s.split("#", 1)[1]
    else:
        s = s.rsplit("/", 1)[-1]
    return urllib.parse.unquote(s)


def node_to_text(g: Graph, node: Any) -> str:
    """Prefer rdfs:label; fall back to local name for URIRefs."""
    if isinstance(node, Literal):
        return str(node).strip()
    if isinstance(node, URIRef):
        for lbl in g.objects(node, RDFS.label):
            text = str(lbl).strip()
            if text:
                return text
        return local_name(node).strip()
    return str(node).strip()


def dedup_stable(items: List[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def gather_synonyms(g: Graph, subject: URIRef) -> List[str]:
    raw = [str(obj).strip() for obj in g.objects(subject, P53)]
    return dedup_stable([s for s in raw if s])


def gather_scientific_description(g: Graph, subject: URIRef) -> str:
    for obj in g.objects(subject, P54):
        return str(obj)
    return ""


def gather_llm_description(g: Graph, subject: URIRef) -> str:
    for obj in g.objects(subject, P55):
        return str(obj)
    return ""


def gather_categories(g: Graph, subject: URIRef) -> List[str]:
    """Collect P48 values; support both Literals and URIRefs."""
    raw: List[str] = []
    for obj in g.objects(subject, P48):
        text = node_to_text(g, obj)
        if text:
            raw.append(text)
    return dedup_stable(raw)


def gather_lower_limit(g: Graph, subject: URIRef) -> Any:
    for obj in g.objects(subject, P65):
        return obj.toPython() if isinstance(obj, Literal) else str(obj)
    return ""


def gather_upper_limit(g: Graph, subject: URIRef) -> Any:
    for obj in g.objects(subject, P66):
        return obj.toPython() if isinstance(obj, Literal) else str(obj)
    return ""


def gather_not_allowed_auxiliary(g: Graph, subject: URIRef) -> List[str]:
    """Collect P68 values, stripped of the PARSEC namespace prefix."""
    raw: List[str] = []
    for obj in g.objects(subject, P68):
        value = str(obj).strip()
        value = value.replace(BASE_IRI, "")
        if value:
            raw.append(value)
    return dedup_stable(raw)


def gather_characterizations(g: Graph, subject: URIRef) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for obj in g.objects(subject, P75):
        char_name = local_name(obj)

        literal_value = ""
        for val in g.objects(obj, P76):
            literal_value = str(val)
            break

        llm_desc = ""
        for desc in g.objects(obj, P77):
            llm_desc = str(desc)
            break

        out.append(
            {
                "name": char_name,
                "literal_value": literal_value,
                "llm_description": llm_desc,
            }
        )
    return out


def gather_follows_base_units(g: Graph, subject: URIRef) -> Optional[bool]:
    for obj in g.objects(subject, P86):
        if isinstance(obj, Literal):
            value = obj.toPython()
            if isinstance(value, bool):
                return value
    return None


def get_category_pertains(g: Graph) -> Dict[str, List[str]]:
    """category_name -> sorted list of allowed celestial-body types (P72)."""
    mapping: Dict[str, List[str]] = {}
    for cat in g.subjects(RDF.type, E22):
        cat_name = local_name(cat)
        if cat_name.startswith("_"):
            continue
        types = {
            str(o).strip().lower()
            for o in g.objects(cat, P72)
            if str(o).strip()
        }
        if types:
            mapping[cat_name] = sorted(types)
    return mapping


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------
def extract_concepts(g: Graph) -> List[Dict[str, Any]]:
    concepts: List[Dict[str, Any]] = []
    for subject in g.subjects(RDF.type, E11):
        if not isinstance(subject, URIRef):
            continue
        concepts.append(
            {
                "Name": local_name(subject),
                "Scientific_Description": gather_scientific_description(g, subject),
                "LLM_Description": gather_llm_description(g, subject),
                "Synonyms": gather_synonyms(g, subject),
                "Categories": gather_categories(g, subject),
                "Lower_Limit": gather_lower_limit(g, subject),
                "Upper_Limit": gather_upper_limit(g, subject),
                "Not_Allowed_Metadata_Concepts": gather_not_allowed_auxiliary(g, subject),
                "Characterizations": gather_characterizations(g, subject),
                "Follows_Base_Units": gather_follows_base_units(g, subject),
            }
        )
    concepts.sort(key=lambda x: x["Name"])
    return concepts


def write_json(concepts: List[Dict[str, Any]], out_path: Path) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(concepts, f, ensure_ascii=False, indent=2)


def write_concepts_tsv(concepts: List[Dict[str, Any]], out_path: Path) -> None:
    fieldnames = ["Concept", "Description", "Synonyms", "Category", "Characterizations"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", delimiter="\t")
        writer.writeheader()

        for item in concepts:
            synonyms = item.get("Synonyms", [])
            synonyms_str = " | ".join(synonyms) if isinstance(synonyms, list) else str(synonyms or "")

            categories = item.get("Categories", [])
            if not isinstance(categories, list):
                categories = [categories] if categories else []

            char_strings = []
            for char in item.get("Characterizations", []):
                char_str = char.get("name", "")
                if char.get("literal_value"):
                    char_str += f" ({char['literal_value']})"
                char_strings.append(char_str)
            characterizations_str = " | ".join(char_strings)

            for category in categories:
                if category.startswith("_"):
                    continue
                writer.writerow(
                    {
                        "Concept": item.get("Name", ""),
                        "Description": item.get("LLM_Description", ""),
                        "Synonyms": synonyms_str,
                        "Category": category,
                        "Characterizations": characterizations_str,
                    }
                )


def write_category_pertains(mapping: Dict[str, List[str]], out_path: Path) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("Category\tPertains_to\n")
        for cat_name, pertains in sorted(mapping.items()):
            f.write(f"{cat_name}\t{', '.join(pertains)}\n")


def write_characterizations(concepts: List[Dict[str, Any]], out_path: Path) -> None:
    char_mapping: Dict[str, List[Dict[str, str]]] = {}
    for item in concepts:
        if item.get("Characterizations"):
            char_mapping[item["Name"]] = item["Characterizations"]
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(char_mapping, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    args = parse_args()
    paths = resolve_paths(args)

    ontology_path: Path = paths["ontology"]
    out_dir: Path = paths["out_dir"]
    concepts_name: str = paths["concepts_name"]

    if not ontology_path.exists():
        raise FileNotFoundError(f"Ontology file not found: {ontology_path}")

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading ontology: {ontology_path}")
    g = Graph()
    g.parse(ontology_path.resolve().as_uri(), format="turtle")

    print("Extracting E11_Concept instances...")
    concepts = extract_concepts(g)

    # 1) Full metadata JSON
    metadata_json = out_dir / "concepts_for_metadata.json"
    write_json(concepts, metadata_json)
    print(f"Wrote {metadata_json} ({len(concepts)} concepts)")

    # 2) Concepts TSV
    tsv_path = out_dir / f"{concepts_name}.tsv"
    write_concepts_tsv(concepts, tsv_path)
    print(f"Wrote {tsv_path}")

    # 3) Category-pertains TSV
    cat_pertains = get_category_pertains(g)
    cat_path = out_dir / "category_pertains.tsv"
    write_category_pertains(cat_pertains, cat_path)
    print(f"Wrote {cat_path} ({len(cat_pertains)} categories)")

    # 4) Characterizations JSON
    char_path = out_dir / "characterizations.json"
    write_characterizations(concepts, char_path)
    print(f"Wrote {char_path}")

    print("Done.")


if __name__ == "__main__":
    main()
