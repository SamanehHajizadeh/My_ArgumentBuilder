import unittest
from aba.rulegenerator import RuleGenerator
from aba.assumptionBaseArg_framework import ABA_framework
class test_MultipleDisputeTrees(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_1(self):
        """
        a1 |- c.
        a2 |- c.
        b1 |- d.
        b2 |- d.
        contrary(a1, d).
        contrary(a2, d).
        contrary(b1, c).
        contrary(b2, c).
        """

        aba = ABA_framework()
        aba.symbols = ('a1', 'a2', 'b1', 'b2', 'c', 'd')
        aba.rules.append(RuleGenerator(['a1'], 'c'))
        aba.rules.append(RuleGenerator(['a2'], 'c'))
        aba.rules.append(RuleGenerator(['b1'], 'd'))
        aba.rules.append(RuleGenerator(['b2'], 'd'))
        aba.contraries['a1'] = 'd'
        aba.contraries['a2'] = 'd'
        aba.contraries['b1'] = 'c'
        aba.contraries['b2'] = 'c'

        aba.extract_assumptions_from_contraries()
