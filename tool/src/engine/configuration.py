'''
Created on Dec 9, 2015

@author: umang
'''

class Configuration:
    '''
    Configuration reperesents the problem under test:
    SHA sha
    Mode target_mode
    we would like to check if starting from some initial mode in sha, is there a run that reaches target_mode 
    '''
    def __init__(self, sha, target_mode):
        '''
        Constructor
        '''
        self.sha = sha
        self.target_mode = target_mode