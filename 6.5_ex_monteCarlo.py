#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""6.5_ex_monteCarlo.py

Code for Pr. L. Jaulin's "rob exo 6.5 : Monte-Carlo", youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Development"
__name__ = "main"

from roblib import *
import numpy as np
import matplotlib.pyplot as plt
import random

n_p = 10000
random_x = [random.uniform(0, 2) for k in range(n_p)]
random_y = [random.uniform(0, 2) for i in range(n_p)]
p_vectors = [(random_x[l], random_y[l]) for l in range(n_p)]
y_list = [0, 1, 2.5, 4.1, 5.8, 7.5]
ym_of_p_list = [[], [], [], [], [], []]
correct_vectors = []
epsilon = 0.5


def simul(steps):
    """

    Args:
        steps:

    Returns:

    """
    for l in range(n_p):
        trigger = True  # to verify that vector p_vectors[l] verifies condition
        a = p_vectors[l][0]
        b = p_vectors[l][1]
        x = array([[0],
                   [0]]
                  )
        u = 1
        y = array([1, 1]) @ x
        m_matrix = array([[1, 0],
                          [a, 0.3]]
                         )
        l_matrix = array([[b],
                          [1 - b]]
                         )
        # --------------------
        ym_of_p_list[0].append(y)
        if not abs(y - y_list[0]) < epsilon:
            trigger = False
        for k in range(1, steps):
            x = m_matrix @ x + l_matrix * u
            y = array([1, 1]) @ x
            if k != 0:
                ym_of_p_list[k].append(y[0])
            if not abs(y - y_list[k]) < epsilon or trigger == False:
                trigger = False
        if trigger == True:
            correct_vectors.append(p_vectors[l])
    return


def ym(number_p, k):
    """

    Args:
        number_p (int): index of desired p vector
        k (int): step number

    Returns:

    """
    return ym_of_p_list[k][number_p]


def draw_selected_p():
    """

    Returns:

    """
    corr_vect_x = [correct_vectors[x][0] for x in range(len(correct_vectors))]
    corr_vect_y = [correct_vectors[x][1] for x in range(len(correct_vectors))]
    plt.plot(corr_vect_x, corr_vect_y, "*b")



if __name__ == "main":
    plt.plot(random_x, random_y, "*k")
    simul(6)
    draw_selected_p()
    pass
