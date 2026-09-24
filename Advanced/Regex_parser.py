import re
import pprint
from Concepts.OntologyProcessing import OntologyParser 


def parse_custom_query(query_string, ontology_parser):

    group_regex = re.compile(
        r"\{([^{}]*)\}\s*(?:(AND\s+NOT|AND|OR))?",
        re.IGNORECASE
    )

    operation_regex = re.compile(
        r"\(((?:[^()]|\([^()]*\))*)\)\s*(?:(AND\s+NOT|AND|OR))?",
        re.IGNORECASE
    )

    details_regex = re.compile(
        r"([^|]+)\|([^|]+)\|([^|]+)\|([^|\s]+)\s+(<=>|<=|>=|==|!=|<|>|str)\s+\[([^\]]+)\]\s+\"([^\"]*)\""
    )

    parsed_data = []
    constraint_id = 0
    group_matches = list(group_regex.finditer(query_string))

    # Track the operator linking from the PREVIOUS group
    previous_outgroup_operator = "AND"

    for group_index, group_match in enumerate(group_matches):
        group_content = group_match.group(1)
        trailing_outgroup_operator = group_match.group(2)

        operation_matches = list(operation_regex.finditer(group_content))
        
        previous_ingroup_operator = "AND"

        for ingroup_index, op_match in enumerate(operation_matches):
            op_content = op_match.group(1).strip()
            trailing_ingroup_operator = op_match.group(2)

            details_match = details_regex.fullmatch(op_content)

            if not details_match:
                raise ValueError(f"Invalid constraint syntax:\n({op_content})")

            auxiliary = details_match.group(1).strip()
            category = details_match.group(2).strip()
            feature = details_match.group(3).strip()
            characterisation = details_match.group(4).strip()
            math_operator = details_match.group(5).strip()
            constraint_val = [value.strip() for value in details_match.group(6).split(",")]
            units = details_match.group(7).strip()

            if not ontology_parser.validate_constraint(auxiliary, category, feature, characterisation, units):
                raise ValueError(f"Invalid ontology mapping:\n({op_content})")

            constraint_id += 1

            constraint = {
                "ID": constraint_id,
                "Category": category,
                "Feature": feature,
                "Characterisation": characterisation,
                "Auxiliary": auxiliary,
                "Math_Operator": math_operator,
                "Constraint_Val": constraint_val,
                "Units": units,
                "Ingroup_Logic_Operator": previous_ingroup_operator.upper().strip(),
                "Outgroup_Logic_Operator": previous_outgroup_operator.upper().strip(),
                "Group_Index": group_index,
                "Ingroup_Index": ingroup_index
            }

            parsed_data.append(constraint)

            if trailing_ingroup_operator:
                previous_ingroup_operator = trailing_ingroup_operator

        if trailing_outgroup_operator:
            previous_outgroup_operator = trailing_outgroup_operator

    return parsed_data

def validate_constraint_values(math_operator, constraint_values):
    if math_operator == "<=>":
        # contain exactly two values
        if len(constraint_values) != 2:
            return False

        try:
            first = float(constraint_values[0])
            second = float(constraint_values[1])
        except ValueError:
            return False

        return first < second


#============================================================
# REMINDER:
# We will use (but needs discussing) different string searches
# Contains inside, strats with, ends with, exact match ect
#============================================================

    elif math_operator == "str":
        # String constraint must contain exactly one value
        if len(constraint_values) != 1:
            return False

        return True

    else:
        if len(constraint_values) != 1:
            return False

        try:
            float(constraint_values[0])
        except ValueError:
            return False

        return True