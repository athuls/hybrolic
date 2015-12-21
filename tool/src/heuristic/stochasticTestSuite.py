'''
Unit tests that exercise the algorithms. It is a mixture of both real 'unit' tests and functional tests of search
'''
import unittest
from heuristic import resultHelpers
class SearchTests(unittest.TestCase):
    
    def setUp(self):
        self.Vector = [1,2]
        # Problem Configuration
        '''For hybrolic, this will be range of n i.e. number of iterations'''
        loopIt = range(1,1000)
        self.POLY = loopIt
        
    #@unittest.skip("Don't run FOR NOW!")          
    def testTabuSearch(self):
        from heuristic.tabuSearch import search
        # Problem Configuration
        # Use Berlin52 instance of TSPLIB
        # Algorithm Configuration
        maxIterations = 100
        maxTabuCount = 15
        maxCandidates = 50
        # Execute the algorithm
        result = search(self.POLY,maxIterations, maxTabuCount, maxCandidates)
        tspResult = TSPResult(7542,"Tabu Search Results")
        print tspResult.FormattedOutput(result)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRandomSeaarch']
    unittest.main()