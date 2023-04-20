import unittest
from aba.rulegenerator import RuleGenerator
from aba.assumptionBaseArg_framework import ABA_framework
from aba.argumet_transformer import Argumet_transformer
import logging


class test_OneArgumentTwoSymbols(unittest.TestCase):

    def setUp(self):

        self.aba = ABA_framework()
        self.aba.symbols = ('a', 'b', 'c')
        self.aba.rules.append(RuleGenerator(['a'], 'b'))
        self.aba.rules.append(RuleGenerator(['b'], 'a'))
        self.aba.rules.append(RuleGenerator([None], 'c'))

        for r in self.aba.rules:
            print(r)

        self.aba.extract_assumptions_from_contraries()
