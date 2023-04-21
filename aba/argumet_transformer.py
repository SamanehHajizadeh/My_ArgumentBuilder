import re

from .assumptionBaseArg_framework import ABA_framework
from .rulegenerator import RuleGenerator


class Argumet_transformer():
    def __init__(self, raw):
        self.raw = raw
        self.__regex_rule = re.compile(r'\s*(?P<symbols>[a-zA-Z0-9 ,]+)?\s*\|-\s*(?P<result>\S+)?\.')
        self.__regex_contrary = re.compile(r'\s*contrary\(\s*(?P<assumption>\S+)\s*,\s*(?P<symbol>\S+)\s*\)\.')
        self.__regex_assumption = re.compile(r'\s*assumption\(\s*(?P<assumption>\S+)\s*\)\.')

        self.parsed_rules = []
        self.parsed_contraries = dict()
        self.parsed_assumptions = []

    def rule_transformer(self, rule_match):
        errors = []
        raw_symbols = rule_match[0]
        result = rule_match[1]

        if raw_symbols:
            symbols = [x.strip() for x in raw_symbols.split(',')]
        else:
            symbols = [None]

        if len(errors) == 0:
            self.parsed_rules.append(RuleGenerator(symbols, result))

        return errors

    def contrary_transformer(self, contary_match):
        errors = []

        assumption = contary_match[0]
        symbol = contary_match[1]

        if len(errors) == 0:
            self.parsed_contraries[assumption] = symbol

        return errors

    def assumption_transformer(self, assumption_match):
        errors = []

        assumption = assumption_match

        if len(errors) == 0:
            self.parsed_assumptions.append(assumption)

        return errors

    def parse(self):
        errors = []

        for j, raw_line in enumerate(self.raw.splitlines()):
            line = raw_line.strip()
            i = j + 1

            if len(line) == 0:
                continue

            line_errors = []
            rule_matches = self.__regex_rule.findall(line)
            contrary_matches = self.__regex_contrary.findall(line)
            assumption_matches = self.__regex_assumption.findall(line)

            if len(line_errors) > 0:
                errors.extend(line_errors)
                continue

            if len(rule_matches) == 1:
                process_errors = self.rule_transformer(rule_matches[0])
                line_errors.extend(["Error: Line %d %s" % (i, x) for x in process_errors])

            elif len(contrary_matches) == 1:
                process_errors = self.contrary_transformer(contrary_matches[0])
                line_errors.extend(["Error: Line %d %s" % (i, x) for x in process_errors])

            elif len(assumption_matches) == 1:
                process_errors = self.assumption_transformer(assumption_matches[0])
                line_errors.extend(["Error: Line %d %s" % (i, x) for x in process_errors])

            errors.extend(line_errors)

        return errors

    def __get_aba_symbols(self):
        symbols = set()

        for rule in self.parsed_rules:
            symbols.add(rule.result)
            for symbol in rule.symbols:
                if symbol is not None:
                    symbols.add(symbol)

        for assumption in self.parsed_assumptions:
            if assumption is not None:
                symbols.add(assumption)

        return tuple(x for x in iter(symbols))

    def construct_builder(self):
        aba = ABA_framework()
        aba.symbols = list(self.__get_aba_symbols())

        for symbol in aba.symbols:
            print("Print all symbols: ", symbol)

        for rule in self.parsed_rules:
            aba.rules.append(rule)
            print("Rule in the way Carlos wish to see:", rule.symbols, "->", rule.result)

        for contrary in self.parsed_contraries:
            print("Contrary of ", contrary, "=", self.parsed_contraries.get(contrary))

        for assumption, symbol in self.parsed_contraries.items():
            aba.contraries[assumption] = symbol

        for assumption in self.parsed_assumptions:
            print("Assumption: ", assumption)
            aba.assumptions.append(assumption)

        aba.extract_assumptions_from_contraries()

        return aba
