'''
Unit tests that exercise the algorithms. It is a mixture of both real 'unit' tests and functional tests of search
'''
import unittest
from . import ResultHelpers
class SearchTests(unittest.TestCase):
    
    def setUp(self):
        self.Vector = [1,2]
        # Problem Configuration
        '''For hybrolic, this will be range of n i.e. number of iterations'''
        berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
                    [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
                    [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
                    [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
                    [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
                    [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
                    [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
                    [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
                    [830,610],[605,625],[595,360],[1340,725],[1740,245]
                   ]
        self.TSPLIB = berlin52
        
    #@unittest.skip("Don't run FOR NOW!")          
    def testTabuSearch(self):
        from .TabuSearch import search
        # Problem Configuration
        # Use Berlin52 instance of TSPLIB
        # Algorithm Configuration
        maxIterations = 100
        maxTabuCount = 15
        maxCandidates = 50
        # Execute the algorithm
        result = search(self.TSPLIB,maxIterations, maxTabuCount, maxCandidates)
        tspResult = TSPResult(7542,"Tabu Search Results")
        print tspResult.FormattedOutput(result)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRandomSeaarch']
    unittest.main()