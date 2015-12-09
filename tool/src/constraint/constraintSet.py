'''
Created on Dec 8, 2015

@author: umang
'''

class ConstraintSet(object):
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