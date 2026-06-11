from Advanced.DSLParser import DSLParser

class QueryParser:
    def __init__(self, input_string):
        self.parser = DSLParser(input_string)

    def parse(self, raw_string=None):
        # allow both styles:
        if raw_string is not None:
            self.parser = DSLParser(raw_string)

        return self.parser.parse()