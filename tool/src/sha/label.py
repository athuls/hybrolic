'''
Created on Dec 8, 2015

@author: umang
'''

class Label:
    '''
    classdocs
    '''
    __labelindex__ = 0
    
    def __init__(self, name=None):
        '''
        Constructor
        '''
        self.index = Label.__labelindex__
        Label.__labelindex__ = Label.__labelindex__ + 1
        if name is None:
            self.name = 'l' + str(self.index)
        else:
            self.name = name
            
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()