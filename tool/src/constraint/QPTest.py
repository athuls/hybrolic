'''
Created on Dec 8, 2015

@author: sandur2
'''
from constraint import Constraint
from QP import QP

c1 = Constraint(4, [1.,0.,0.,0.], [3.])
c2 = Constraint(4, [-1.,0.,0.,0.], [0.])
c3 = Constraint(4, [0.,1.,0.,0.], [3.])
c4 = Constraint(4, [0.,-1.,0.,0.], [0.])
c5 = Constraint(4, [0.,0.,1.,0.], [7.])
c6 = Constraint(4, [0.,0.,-1.,0.], [-4.])
c7 = Constraint(4, [0.,0.,0.,1.], [7.])
c8 = Constraint(4, [0.,0.,0.,-1.], [-4.])

qp = QP(4)
qp.add_constraint(c1)
qp.add_constraint(c2)
qp.add_constraint(c3)
qp.add_constraint(c4)
qp.add_constraint(c5)
qp.add_constraint(c6)
qp.add_constraint(c7)
qp.add_constraint(c8)
sol = qp.solve()
print(sol['x'])