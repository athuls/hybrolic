'''
Created on Dec 8, 2015

@author: umang
'''

from error.error import Error

class Constraint:
    '''
    Denotes a single linear constraint
    of the form
    a1 x1 + a2 x2 + ... an xn <= b
    
    Here,
    num_vars = n
    coefficients = [a1, a2, ..., an]
    constant = b
    '''
    
    @staticmethod
    def check_dim_static(n1, n2):
        if(n1 != n2):
            Error.error("Dimension mismatch")

    def __init__(self, num_vars, coefficients, constant):
        '''
        Constructor
        '''
        self.num_vars = num_vars
        self.check_dim(len(coefficients))
        self.coefficients = coefficients
        self.constant = constant
        
    def check_dim(self, n):
        '''Constraint.check_dim_static(self.num_vars, n)'''
        if(self.num_vars != n):
            Error.error("Dimension mismatch")