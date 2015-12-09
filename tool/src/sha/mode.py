'''
Created on Dec 8, 2015

@author: umang
'''
from sets import Set
from error.error import Error

class Mode:
    '''
    classdocs
    '''
    __modeindex__ = 0
    def __init__(self, num_vars, flow_vector, name=None):
        '''
        Constructor
        '''
        if (num_vars != len(flow_vector)):
            Error.error("Mismatch between dimensions of flow_vector and num_vars ")
           
        self.index = Mode.__modeindex__
        Mode.__modeindex__ = Mode.__modeindex__ + 1 
        self.num_vars = num_vars
        self.flow_vector = flow_vector
        if name is None:
            self.name = 'm' + self.index
        else:
            self.name = name
        self.invariant = None
        
        self.from_neighbor_list = []
        self.to_neighbor_list = []
        self.neighbor_list = []
        self.in_transition_list = []
        self.out_transition_list = []
        self.transition_list = []
        
    def set_invariant(self, invariant):
        self.invariant = invariant
        
    def add_in_transition(self, trans):
        from_neighbor = trans.from_mode
        self.from_neighbor_list = list(Set(self.from_neighbor_list.append(from_neighbor)))
        self.neighbor_list = list(Set(self.neighbor_list.append(from_neighbor)))
        self.in_transition_list = list(Set(self.in_transition_list.append(trans)))
        self.transition_list = list(Set(self.transition_list.append(trans)))
        
    def add_out_transition(self, trans):
        to_neighbor = trans.to_mode
        self.to_neighbor_list = list(Set(self.to_neighbor_list.append(to_neighbor)))
        self.neighbor_list = list(Set(self.neighbor_list.append(to_neighbor)))
        self.out_transition_list = list(Set(self.out_transition_list.append(trans)))
        self.transition_list = list(Set(self.transition_list.append(trans)))
        
    def add_transition(self, trans):
        from_neighbor = trans.from_mode
        if(from_neighbor == self):
            self.add_out_transition(trans)
        to_neighbor = trans.to_mode
        if(to_neighbor == self):
            self.add_in_transition(trans)
            
    def add_transition_list(self, tlist):
        for trans in tlist:
            self.add_transition(trans)
        
    def to_string(self):
        string_rep = ''
        string_rep = string_rep + 'Mode ' + self.name + ':' + '\n'
        string_rep = string_rep + 'Flow Vector = ' + self.flow_vector + '\n'
        string_rep = string_rep + 'Invariant : \n ' + self.invariant + '\n'
        
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.__str__()
        
