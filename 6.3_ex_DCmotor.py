#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""1.10_ex_auv3d.py

Slight adaptation of Pr. L. Jaulin's "rob exo 1.10 : 3D robot graphics",

Roblib package function dot will be used alongside natural python array
multiplication operator @ without distinction

Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *

y = array([5, 10, 8, 14, 17]).transpose()
m = array([[4, 0],
           [10, 1],
           [10, 5],
           [13, 5],
           [15, 3]
           ]
          )

k = inv((m.transpose() @ m)) @ m.transpose()
print("p_chap is", k @ y)  # p_chap
p1chap = 1.18831169
p2chap = -0.51688312


def f(u, tr):
    """

    Args:
        u:
        tr:

    Returns:

    """
    return p1chap * u + p2chap * tr


list_U = [m[i][0] for i in range(m.shape[0])]
liste_Tr = [m[i][1] for i in range(m.shape[0])]

for i in range(len(list_U)):
        print(f(list_U[i], liste_Tr[i]))

y_chap = array([f(list_U[i], liste_Tr[i])
                for i in range(len(list_U))]).transpose()
print("residal vector", y - y_chap)

print("estimated angular speed is", f(20, 10))
