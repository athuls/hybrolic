'''
Created on Dec 8, 2015

@author: umang
'''

from cvxopt import matrix, solvers 

class ConstraintSet:
    '''
    classdocs
    '''
    
    def __init__(self, num_vars):
        '''
        Constructor
        '''
        self.num_vars = num_vars
        
    def add_constraint(self, constraint):
        constraint.check_dim(self.num_vars)
        self.constraintList.append(constraint)
        
    def get_LP(self):
        A = []
        b = []
        for c in self.constraintList:
            A.append(c.coefficients)
            b.append(c.constant)
        return (A,b)
    
    '''Will need to factor it out into separate class'''
    def feasible(self):
        '''Return solution of LP'''
        G,h = self.get_LP()
        GMatrix = matrix(G)
        hMatrix = matrix(h)
                
        '''Dummy objective function to check for feasibility'''
        c = matrix([1])
        sol = solvers.lp(c, GMatrix, hMatrix)
        if(sol == None):
            return False
        
    def distance(self):
        if(self.feasible()):
            