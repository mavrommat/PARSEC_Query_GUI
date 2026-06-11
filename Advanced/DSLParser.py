import re
import json

class DSLParser:
    def __init__(self, input_string):
        self.tokens = self.tokenize(input_string)
        self.pos = 0

    # ---------------- TOKENIZER ----------------
    def tokenize(self, input_string):
        token_specification = [
            ('GROUP_START', r'[\(\{]'),
            ('GROUP_END',   r'[\)\}]'),
            ('LOGIC',       r'\b(AND NOT|OR NOT|AND|OR|NOT)\b'),
            ('OP',          r'<=>|>=|<=|==|!=|>|<|~=|\bIN\b'),
            ('VAL',         r'\[[^\]]+\]|-?\d*\.?\d+(?:[eE][-+]?\d+)?'),
            ('VAR',         r'[a-zA-Z_][a-zA-Z0-9_\.]*'),
            ('UNIT',        r'"(?:All_units|No_units)"|[a-zA-Z_0-9\-\/\^]+'),
            ('SKIP',        r'[ \t\n]+'),
            ('MISMATCH',    r'.'),
        ]

        tok_regex = '|'.join(
            f'(?P<{name}>{regex})' for name, regex in token_specification
        )

        tokens = []
        for mo in re.finditer(tok_regex, input_string):
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'SKIP':
                continue
            if kind == 'MISMATCH':
                raise RuntimeError(f"Unexpected character: {value}")

            tokens.append((kind, value))

        return tokens

    # ---------------- UTIL ----------------
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def match(self, *kinds):
        tok = self.peek()
        if tok and tok[0] in kinds:
            return True
        return False

    # ---------------- ENTRY ----------------
    def parse(self):
        ast = self.parse_expr()
        return ast

    # ---------------- GRAMMAR ----------------
    # expr := term (OR term)*
    def parse_expr(self):
        nodes = [self.parse_term()]

        # FIX: Accept both OR and OR NOT
        while self.match('LOGIC') and self.peek()[1] in ['OR', 'OR NOT']:
            logic_op = self.advance()[1]
            nodes.append({"logic": logic_op})
            nodes.append(self.parse_term())

        return self.flatten(nodes)

    def parse_term(self):
        nodes = [self.parse_factor()]

        # FIX: Accept both AND and AND NOT
        while self.match('LOGIC') and self.peek()[1] in ['AND', 'AND NOT']:
            logic_op = self.advance()[1]
            nodes.append({"logic": logic_op})
            nodes.append(self.parse_factor())

        return self.flatten(nodes)
    
    # factor := NOT factor | group | condition
    def parse_factor(self):
        if self.match('LOGIC') and self.peek()[1] == 'NOT':
            self.advance()
            # We MUST parse the next factor that is being negated!
            factor = self.parse_factor()
            
            # Preserve the flat array shape required by parse_term / parse_expr
            if isinstance(factor, list):
                return [{"logic": "NOT"}] + factor
            return [{"logic": "NOT"}, factor]

        if self.match('GROUP_START'):
            return self.parse_group()

        return self.parse_condition()

    # group := { expr }
    def parse_group(self):
        self.advance()  # consume '{' or '('
        content = self.parse_expr()
        if not self.match('GROUP_END'):
            raise RuntimeError("Unclosed group")
        self.advance()

        return {
            "type": "group",
            "elements": content if isinstance(content, list) else [content]
        }

    # condition := VAR OP VAL UNIT?
    def parse_condition(self):
        cond = {}

        tok = self.advance()
        if tok[0] != 'VAR':
            raise RuntimeError("Expected variable")

        cond['variable'] = tok[1]

        tok = self.advance()
        if tok[0] != 'OP':
            raise RuntimeError("Expected operator")

        cond['operator'] = tok[1]

        tok = self.advance()
        if tok[0] != 'VAL':
            raise RuntimeError(f"Expected value, got {tok[0]}")

        raw = tok[1]
        
        # If the operator is ~=, parse as raw strings 
        if raw.startswith('['):
            raw = raw.strip('[]')
            if cond['operator'] == '~=':
                cond['value'] = [v.strip() for v in raw.split(',') if v.strip()]
            else:
                cond['value'] = [float(v.strip()) for v in raw.split(',') if v.strip()]
        else:
            if cond['operator'] == '~=':
                cond['value'] = [raw.strip()]
            else:
                cond['value'] = [float(raw.strip())]

        # Since your units are now strictly enclosed in quotes (e.g., "All_units"),
        # we only need to grab the single token.
        if self.match('UNIT', 'VAR'):
            cond['unit'] = self.advance()[1]

        return cond

    def flatten(self, nodes):
        out = []

        for n in nodes:
            if isinstance(n, list):
                out.extend(n)
            else:
                out.append(n)

        return out


