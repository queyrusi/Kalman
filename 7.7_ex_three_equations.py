#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.7_ex_three_equations.py

Code for Pr. L. Jaulin's "rob exo 7.10 : estimateur 3 equations",
youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *

if __name__ == "main":
    y = array([[8, 7, 0]]).transpose()
    c_matrix = array([[2, 3],
                      [3, 2],
                      [1, -1]]
                     )
    x_bar = array([[0, 0]]).transpose()
    gamma_x = array([[10000, 0],
                     [0, 10000]]
                    )
    y_bar = c_matrix @ x_bar
    y_tilde = y - c_matrix @ x_bar
    gamma_beta = array([[1, 0, 0],
                        [0, 4, 0],
                        [0, 0, 4]]
                       )
    gamma_y = c_matrix @ gamma_x @ c_matrix.transpose() + gamma_beta
    k_matrix = gamma_x @ c_matrix.transpose() @ inv(gamma_y)
    x_hat = x_bar + k_matrix @ y_tilde
    gamma_epsilon = gamma_x - k_matrix @ c_matrix @ gamma_x

    p_hat = inv(c_matrix.transpose() @ c_matrix) @ c_matrix.transpose() @ y