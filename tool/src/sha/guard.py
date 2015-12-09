'''
Created on Dec 8, 2015

@author: umang
'''
from constraint.constraintSet import ConstraintSet

class Guard(ConstraintSet):
    '''
    classdocs
    '''

    def __init__(self, num_vars, clist=None):
        '''
        Constructor
        '''
        ConstraintSet.__init__(self, num_vars, clist)