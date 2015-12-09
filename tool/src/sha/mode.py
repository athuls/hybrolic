'''
Created on Dec 8, 2015

@author: umang
'''
from error.error import Error

class Mode:
    '''
    classdocs
    '''
    
    def __init__(self, num_vars, flow_vector):
        '''
        Constructor
        '''
        if (num_vars != len(flow_vector)):
            Error.error("Mismatch between dimensions of flow_vector and num_vars ")
            
        self.num_vars = num_vars
        self.flow_vector = flow_vector
        
    def add_into_transition(self, trans):
        '''do something'''
        