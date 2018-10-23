#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.8_ex_motor.py

Code for Pr. L. Jaulin's "exo 7.8 : estimateur lineaire moteur",
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
    # measurements:
    y = array([[5, 10, 8, 14, 17]]).transpose()

    # linear system matrix
    c_matrix = array([[4, 0],
                      [10, 1],
                      [10, 5],
                      [13, 5],
                      [15, 3]]
                     )

    # mean parameters
    # is given when we have an idea of x1 and x2  (parameters). Should be taken
    # at [0, 0] when in doubt.
    x_bar = array([[1, -1]]).transpose()

    # parameters covariance matrix
    # is given when we have an idea of x1 and x2  (parameters) with an
    # associated variance. Should be taken at inf * I when in doubt.
    gamma_x = array([[4, 0],
                     [0, 4]]
                    )

    # mean measurements
    y_bar = c_matrix @ x_bar

    # innovation:
    y_tilde = y - c_matrix @ x_bar

    gamma_beta = 9 * eye(5)  # déterminée dans l'ennonce (y = C * x + beta)

    # covariance of the innovation:
    gamma_y = c_matrix @ gamma_x @ c_matrix.transpose() + gamma_beta

    # Kalman gain:
    k_matrix = gamma_x @ c_matrix.transpose() @ inv(gamma_y)

    # estimated parameters:
    x_hat = x_bar + k_matrix @ y_tilde

    # covariance of the error:
    gamma_epsilon = gamma_x - k_matrix @ c_matrix @ gamma_x  # déduite

    # estimated measurements:
    y_hat = c_matrix @ x_hat

    residual_vector = y - y_hat

    # p_hat = inv(c_matrix.transpose() @ c_matrix) @ c_matrix.transpose() @ y