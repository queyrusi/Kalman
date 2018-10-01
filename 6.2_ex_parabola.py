#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""6.2_ex_parabola.py

Code for Pr. L. Jaulin's "rob exo 6.2 : parabole", youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *

p_hat = array([[0], [0], [0]])
y = array([[17], [3], [1], [5], [11], [46]])
m = array([[9, -3, 1],
           [1, -1, 1],
           [0, 0, 1],
           [4, 2, 1],
           [9, 3, 1],
           [36, 6, 1],
           ]
          )
K = inv((m.transpose() @ m)) @ m.transpose()
p_chap = K @ y
# print(K @ y)  # p_chap

# we find p1chapeau = 1.41
# p2chap = -0.98
# p3chap = 1.06


def f(t):
    """

    Args:
        t:

    Returns:

    """
    return p_chap[0][0] * t ** 2 + p_chap[1][0] * t + p_chap[2][0]


def print_filtered_measurements():
    """

    Returns:

    """
    for t in [-3, -1, 0, 2, 3, 6]:
        print(f(t))
    return


def residual_vector():
    """

    Returns:

    """
    f_vector = list()
    y_vector = [17, 3, 1, 5, 11, 46]
    for t in [-3, -1, 0, 2, 3, 6]:
        f_vector.append(f(t))
    r_vector = [f_vector[i] - y_vector[i] for i in range(len(f_vector))]
    return r_vector
