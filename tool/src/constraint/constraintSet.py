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