Run:
Open terminal
go to path
run python3 main.py
To assurance the functionality of methods u can run all unitTests.


Description Of ABA:
Assumption-based Argumentation(ABA) consists of (L, R, A, -)
"L" is sentences (R + A)
"R" stands for rules (RuleGenerators)
"A" is assumptions A<H,h>
"-" is contrary set, mapped from Assumption to Language that (assumptions attacks another one)

Structure:

MAIN CLASS --> ABA_framework()
arguments : list <ABA_graph>
assumptions: list<String>
nonAssumptions: list<String>
potential_arguments : list<ABA_Graph>
symbols : list<String>
rules: list<RuleGenerator>
contraries : dict(String, string) // value in symbols that attach it's assumption //KEY is an assumption.


Methods:

flag_for_contrary(self):
#Each assumption must have a contrary.

extract_assumptions_from_contraries():
#infer_assumptions to extract the assumptions from the contraries


CLASS --> RuleGenerator()
“symbols”: a list representing the symbols supporting the result of this rule
“result” : a string representing the result or claim or conclusion of this rule

If “symbols” is an empty list => the rule represents a ground truth.

Methods:
“is_ground_truth” : returns a Boolean, if  rule is a ground truth or not.

class -> Argumet_transformer()
represents arguments of the same claim symbol in ABA.

requires an ABA object and a string representing argument claim symbol,in which the argument tree is to be constructed.
The class constructor will call the construction of the argument trees, extraction of assumption set of each argument, and conflict-free and stable semantics computation for each argument.
This class contains the following public properties, which are available for usage after the class has been instantiated:


