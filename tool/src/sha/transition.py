'''
Created on Dec 8, 2015

@author: umang
'''

class Transition:
    '''
    classdocs
    '''
    __transitionindex__ = 0
    def __init__(self, from_mode, guard, label, reset, to_mode, name = None):
        '''
        Constructor
        '''
        self.index = Transition.__transitionindex__
        Transition.__transitionindex__ = Transition.__transitionindex__ + 1
        
        self.from_mode = from_mode
        self.guard = guard
        self.label = label
        self.reset = reset
        self.to_mode = to_mode
        
        if name is None:
            self.name = 'T' + self.index
        else:
            self.name = name
        
    def to_string(self):
        string_rep = 'Transition ' + self.name + ':'
        string_rep = string_rep + '('
        string_rep = string_rep + self.to_mode.name
        #string_rep = string_rep + ', ' + str(self.guard)
        string_rep = string_rep + ', ' + str(self.label)
        string_rep = string_rep + ', ' + self.from_mode.name
        string_rep = string_rep + ')'
        
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.__str__()