'''
Created on Dec 8, 2015

@author: sandur2
[This class is not ready to use]
'''

from cvxopt import matrix, solvers

class QP:
    '''
    classdocs
    '''
    
    def __init__(self, num_vars, clist=None):
        '''
        Constructor
        '''
        self.constraintList=[]
        self.num_vars = num_vars
        if not(clist is None):
            self.add_constraint_list(clist)
        
    def add_constraint(self, constraint):
        constraint.check_dim(self.num_vars)
        self.constraintList.append(constraint)
        
    def add_constraint_list(self, clist):
        for c in clist:
            self.add_constraint(c)
        
    def get_LP(self):
        A = []
        b = []
        for c in self.constraintList:
            A.append(c.coefficients)
            b.append(c.constant)
        return (A,b)
    
    def to_string(self):
        return '\n'.join(self.constraintList)
    
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.__str__()

    def solve(self):
        '''Return solution of LP'''
        '''optimizing dummy variable for LP'''
        PObjective = 2*matrix([ [1., 0., -1., 0.], [0., 1., 0., -1.], [-1., 0., 1., 0.], [0., -1., 0., 1.] ])
        qObjective = matrix([0., 0., 0., 0.])
        [A,b] = self.get_LP()
        AMatrix = matrix(A)
        GConstraints = AMatrix.trans()
        hConstraints = matrix(b).trans()
        sol = solvers.qp(PObjective, qObjective, GConstraints, hConstraints)
        return sol