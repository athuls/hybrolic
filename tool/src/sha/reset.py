'''
Created on Dec 8, 2015

@author: umang
'''

from sets import Set
from error.error import Error

class ResetSet:
    '''
    classdocs
    '''

    def __init__(self, num_vars, rSet=None):
        '''
        Constructor
        '''
        if rSet == None:
            self.rSet = []
        else:
            self.rSet = list(Set(rSet))
            is_valid_set = True
            for x in self.rSet:
                if not (x >=0 and x < self.num_vars):
                    is_valid_set = False
                    break
            if (not is_valid_set):
                Error.error("Invalid Reset Set"  + str(self.rSet))