#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.11_ex_kalm3steps.py

Code for Pr. L. Jaulin's "rob exo 7.11 : Kalman 3 steps",
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
    # parameters for Kalman filter:
    x_0_minus1 = array([[0.],
                        [0.]]
                       )
    gamma_0_minus1 = array([[100, 0],
                            [0, 100]]
                           )
    u_0 = array([[8],
                 [16]]
                )
    u_1 = array([[-6],
                 [-18]]
                )
    u_2 = array([[32],
                 [-8]]
                )
    y_0 = 7
    y_1 = 30
    y_2 = -6
    gamma_alpha_matrix = array([[1, 0],
                                [0, 1]]
                               )
    gamma_beta_0 = array([[1.]])  # !! scalar
    a_0 = array([[0.5, 0],
                 [0, 1]]
                )
    a_1 = array([[1, -1],
                 [1, 1]]
                )
    a_2 = array([[1, -1],
                 [1, 1]]
                )

    c_matrix_0 = array([[1., 1.]])
    c_matrix_1 = array([[1., 1.]])
    c_matrix_2 = array([[1., 1.]])

    ax = init_figure(-100, 100, -100, 100)

    draw_ellipse(x_0_minus1, gamma_0_minus1, 0.99, ax, 'yellow')

    # the x0 in kalman argument is actually x_hat_0/minus1
    x_hat_1, gamma_1 = kalman(x_0_minus1, gamma_0_minus1, u_0, y_0,
                              gamma_alpha_matrix, gamma_beta_0, a_0, c_matrix_0
                              )

    draw_ellipse(x_hat_1, gamma_1, 0.99, ax, 'red')

    x_hat_2, gamma_2 = kalman(x_hat_1, gamma_1, u_1, y_1, gamma_alpha_matrix,
                              gamma_beta_0, a_1, c_matrix_1)

    draw_ellipse(x_hat_2, gamma_2, 0.99, ax, 'green')

    x_hat_3, gamma_3 = kalman(x_hat_2, gamma_2, u_2, y_2, gamma_alpha_matrix,
                              gamma_beta_0, a_2, c_matrix_2)

    draw_ellipse(x_hat_3, gamma_3, 0.99, ax, 'blue')

    # we see the solution is moving in |R2, and that the confidence ellipses are
    # decreasing at each step (det k=0 > det k=1 > det k=2 ...)
