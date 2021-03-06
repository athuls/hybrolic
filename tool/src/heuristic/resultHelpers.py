class TSPResult(object):
    '''
    Class that takes a result from a search algorithm for TSP and prints
    the result and efficacy
    '''


    def __init__(self, optimalTourCost,searchAlgorithm):
        '''
        Constructor
        '''
        self.OptimalTourCost = optimalTourCost
        self.Algorithm = searchAlgorithm
        
    def FormattedOutput(self, result):
        '''
        Calculates the efficacy of the search from the passed in result object, 
        which contains the tour cost of the final solution
        The optimal tour distance for e.g. berlin52 is 7542 units
        Search efficacy is defined as how far we are away from the optimal
        efficacy = (tourCost - optimal)/optimal
        an efficacy of 0 is best
        '''
        name = self.Algorithm
        divider = "*" * 20
        tourCostHeader = "Tour Cost"
        tourCost = round(result["cost"],2)
        
        efficacyHeader = "Search Efficacy"
        efficacy = round(float((result["cost"] - self.OptimalTourCost)/self.OptimalTourCost),2)
        
        final = divider + "\n"\
                + name + "\n"\
                + divider + "\n"\
                + divider + "\n"\
                + tourCostHeader + "\n"\
                + divider + "\n"\
                + str(tourCost) + "\n"\
                + divider + "\n"\
                + efficacyHeader + "\n"\
                + divider + "\n"\
                + str(efficacy) + "\n"\
                + divider + "\n"\
                + divider + "\n"
                
        return final