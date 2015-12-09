'''
Created on Dec 8, 2015

@author: umang
'''

from cvxopt import matrix, solvers 

class ConstraintSet:
    '''
    classdocs
    '''
    def __init__(self, num_vars, clist=None):
        '''
        Constructor
        '''
        self.num_vars = num_vars
        if not(clist is None):
            self.add_constraint_list(clist)
        
    def add_constraint(self, constraint):
        constraint.check_dim(self.num_vars)
        self.constraintList.append(constraint)
        
    def add_constraint_list(self, clist):
        for c in clist:
            self.add_constraint(c)
        
    def get_LP(self):
        A = []
        b = []
        for c in self.constraintList:
            A.append(c.coefficients)
            b.append(c.constant)
        return (A,b)
    
    def to_string(self):
        return '\n'.join(self.constraintList)
    
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.__str__()

    def solve(self):
        '''Return solution of LP'''
        get_LP(self,)
