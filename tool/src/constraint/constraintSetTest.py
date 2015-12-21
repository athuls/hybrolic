'''
Created on Dec 8, 2015

@author: sandur2
'''

#import constraint
from constraint import Constraint
from constraintSet import ConstraintSet

#import constraintSet

#from constraintSet import ConstraintSet

c1 = Constraint(2, [2.,1.], [3.])
c2 = Constraint(2, [1.,2.], [3.])
c3 = Constraint(2, [-1.,0.], [0.])
c4 = Constraint(2, [0.,-1.], [0.])
cSet = ConstraintSet(2)
cSet.add_constraint(c1)
cSet.add_constraint(c2)
cSet.add_constraint(c3)
cSet.add_constraint(c4)
sol = cSet.solve([1.,0.])
if(sol['status']!='optimal'):
    print("Infeasible")
else:
    print("Feasible")

c5 = Constraint(1, [-1.], [-1.])
c6 = Constraint(1, [1.], [-2.])
cSet1 = ConstraintSet(1)
cSet1.add_constraint(c5)
cSet1.add_constraint(c6)
sol1 = cSet1.solve([1.])
if(sol1['status']!='optimal'):
    print("Infeasible")
else:
    print("Feasible")
