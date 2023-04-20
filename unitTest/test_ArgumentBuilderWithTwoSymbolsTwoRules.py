import unittest
from aba.rulegenerator import RuleGenerator
from aba.assumptionBaseArg_framework import ABA_framework


class test_ArgumentBuilderWithTwoSymbolsTwoRules(unittest.TestCase):
    def setUp(self):
        self.aba = ABA_framework()
        self.aba.symbols = ('a', 'b')
        self.aba.rules.append(RuleGenerator(['a'], 'b'))
        self.aba.rules.append(RuleGenerator(['b'], 'a'))

        self.aba.extract_assumptions_from_contraries()

    def test_successful_inference(self):
        self.assertEqual(self.aba.arguments, [])
