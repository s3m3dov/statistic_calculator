import unittest
# Importing Functions
from probability_lib.comb_per import combination, permutation
# Combination & Permutation Test
class CombPerTest(unittest.TestCase):
    def test_comb_basic(self):
        self.assertEqual(combination(6, 2), 15)
    def test_comb_same(self):
        self.assertEqual(combination(4, 4), 1)
    def test_per_basic(self):
        self.assertEqual(permutation(6, 2), 30)

#Main
unittest.main()