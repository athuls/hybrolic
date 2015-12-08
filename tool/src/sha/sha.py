'''
Created on Dec 8, 2015

@author: umang
'''

class sha:
    '''
    classdocs
    '''
    def __init__(self, num_modes, num_vars):
        '''
        Constructor
        '''
        self.num_modes = num_modes
        self.num_vars = num_vars
    
    def add_mode(self, m):
        self.modeList.append(m)
        
    def add_transition(self, transition):
        self.transitionList.append(transition)
        
    