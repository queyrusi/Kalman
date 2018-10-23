#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.9_ex_trochoid.py

Code for Pr. L. Jaulin's "exo 7.9 : trochoid",
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
    y = array([[0.38, 3.25, 4.97, -0.26]]).transpose()
    t = [1, 2, 3, 7]
    c_matrix = array([[1, cos(t[0])],
                      [1, cos(t[1])],
                      [1, cos(t[2])],
                      [1, cos(t[3])]]
                     )

    p_bar = array([[0, 0]]).transpose()
    gamma_x = array([[10000, 0],
                     [0, 10000]]
                    )
    y_bar = c_matrix @ p_bar
    # innovation:
    y_tilde = y - c_matrix @ p_bar
    gamma_beta = 0.01 * eye(4)
    gamma_y = c_matrix @ gamma_x @ c_matrix.transpose() + gamma_beta
    k_matrix = gamma_x @ c_matrix.transpose() @ inv(gamma_y)
    # estimated parameters:
    p_hat = p_bar + k_matrix @ y_tilde
    gamma_epsilon = gamma_x - k_matrix @ c_matrix @ gamma_x
    y_hat = c_matrix @ p_hat
    residual_vector = y - y_hat

    # p_hat = inv(c_matrix.transpose() @ c_matrix) @ c_matrix.transpose() @ y

    time_mesh = arange(0, 10, 0.01)
    absc = p_hat[0] * time_mesh - p_hat[1] * sin(time_mesh)
    ord = p_hat[0]  - p_hat[1] * cos(time_mesh)
    plot(absc, ord, "blue")