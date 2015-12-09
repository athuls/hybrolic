'''
Created on Dec 8, 2015

@author: umang
'''

class Transition:
    '''
    classdocs
    '''
    __transitionindex__ = 0
    def __init__(self, from_mode, guard, label, reset_set, to_mode):
        '''
        Constructor
        '''
        self.index = Transition.__transitionindex__
        Transition.__transitionindex__ = Transition.__transitionindex__ + 1