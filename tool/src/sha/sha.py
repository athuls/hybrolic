'''
Created on Dec 8, 2015

@author: umang
'''

class SHA:
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
        
    def add_transition(self, trans):
        self.transitionList.append(trans)
        
    def set_mode_list(self, mlist):
        self.modeList = mlist
    
    def set_transition_list(self, tlist):
        self.transitionList = tlist
        
    def set_initial_modelist(self, ilist):
        self.initModeList = ilist