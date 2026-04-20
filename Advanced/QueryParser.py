import re

class QueryParser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

        self.constraint_pattern = re.compile(r"""
            \(\s*
            (?P<category>\w+)\.(?P<concept>\w+)\s+
            (?P<relation>>=|<=|>|<|==|IN)\s+
            (?P<value>\[.*?\]|[-+]?\d*\.?\d+(?:e[-+]?\d+)?)\s+
            (?P<unit>[^)]+?)
            \s*\)
        """, re.VERBOSE)

    # ---------------- TOKENIZER ---------------- #

    def tokenize(self, text):
        token_spec = [
            ("CONSTRAINT", r"\([^)]+\)"),   
            ("LPAREN", r"\("),
            ("RPAREN", r"\)"),
            ("AND", r"\bAND\b"),
            ("OR", r"\bOR\b"),
            ("NOT", r"\bNOT\b"),
            ("SKIP", r"\s+"),
        ]

        regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_spec)

        tokens = []
        for match in re.finditer(regex, text):
            kind = match.lastgroup
            value = match.group()
            if kind != "SKIP":
                tokens.append((kind, value))

        return tokens

    # ---------------- CORE PARSER ---------------- #

    def parse(self, text):
        """
        Entry point: handles { ... } OR { ... }
        """
        groups = re.findall(r"\{(.*?)\}", text, re.DOTALL)

        if not groups:
            raise ValueError("No valid groups '{}' found in query.")

        parsed_groups = []
        for g in groups:
            self.tokens = self.tokenize(g)
            self.pos = 0
            parsed_groups.append(self.parse_expression())

        return {
            "type": "OR",
            "children": parsed_groups
        }

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of input")

        if expected and token[0] != expected:
            raise ValueError(f"Expected {expected}, got {token}")

        self.pos += 1
        return token

    # ---------------- GRAMMAR ---------------- #

    def parse_expression(self):
        node = self.parse_term()

        while self.peek() and self.peek()[0] == "OR":
            self.consume("OR")
            right = self.parse_term()
            node = {
                "type": "OR",
                "left": node,
                "right": right
            }

        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.peek() and self.peek()[0] == "AND":
            self.consume("AND")
            right = self.parse_factor()
            node = {
                "type": "AND",
                "left": node,
                "right": right
            }

        return node

    def parse_factor(self):
        token = self.peek()

        if token[0] == "NOT":
            self.consume("NOT")
            return {
                "type": "NOT",
                "child": self.parse_factor()
            }

        elif token[0] == "LPAREN":
            self.consume("LPAREN")
            node = self.parse_expression()
            self.consume("RPAREN")
            return node

        elif token[0] == "CONSTRAINT":
            return self.parse_constraint()

        else:
            raise ValueError(f"Unexpected token: {token}")

    # ---------------- CONSTRAINT ---------------- #

    def parse_constraint(self):
        token = self.consume("CONSTRAINT")
        text = token[1]

        match = self.constraint_pattern.search(text)
        if not match:
            raise ValueError(f"Invalid constraint format: {text}")

        value = match.group("value")

        if value.startswith("["):
            value = [float(x.strip()) for x in value.strip("[]").split(",")]
        else:
            value = float(value)

        return {
            "type": "constraint",
            "category": match.group("category"),
            "concept": match.group("concept"),
            "relation": match.group("relation"),
            "value": value,
            "unit": match.group("unit").strip()
        }