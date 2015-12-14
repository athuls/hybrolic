'''
Created on Dec 8, 2015

@author: sandur2
'''

from cvxopt import matrix, solvers
import constraint
import constraintSet
print("hey")
c1 = constraint.Constraint(2, [2.,1.], [3.])
c2 = constraint.Constraint(2, [1.,2.], [3.])
c3 = constraint.Constraint(2, [-1.,0.], [0.])
c4 = constraint.Constraint(2, [0.,-1.], [0.])
cSet = constraintSet.ConstraintSet(2)
cSet.add_constraint(c1)
cSet.add_constraint(c2)
cSet.add_constraint(c3)
cSet.add_constraint(c4)
sol = cSet.solve()
print(sol)