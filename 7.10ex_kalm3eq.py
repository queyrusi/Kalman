#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.10_ex_kalm3eq.py

Code for Pr. L. Jaulin's "exo 7.7 : Kalman 3 équations",
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
    x0 = array([[0.],
                [0.]]
               )
    gamma_0_matrix = array([[1000, 0],
                            [0, 1000]]
                           )
    u = array([[0]])
    y = array([[8.],
               [7.],
               [0.]]
              )
    gamma_alpha_matrix = array([[0, 0],
                                [0, 0]]
                               )
    gamma_beta_0 = array([[1.]])  # !! scalar
    gamma_beta_1 = array([[4.]])
    gamma_beta_2 = array([[4.]])
    a_matrix = eye(2)
    c_matrix_0 = array([[2., 3.]])
    c_matrix_1 = array([[3., 2.]])
    c_matrix_2 = array([[1., -1.]])

    ax = init_figure(-100, 100, -100, 100)

    draw_ellipse(x0, gamma_0_matrix, 0.99, ax, 'yellow')

    # the x0 in kalman argument is actually x_hat_0
    x_hat_1, gamma_1 = kalman(x0, gamma_0_matrix, u, y[0], gamma_alpha_matrix,
                              gamma_beta_0, a_matrix, c_matrix_0
                              )

    draw_ellipse(x_hat_1, gamma_1, 0.99, ax, 'red')

    x_hat_2, gamma_2 = kalman(x_hat_1, gamma_1, u[0], y[1], gamma_alpha_matrix,
                              gamma_beta_1, a_matrix, c_matrix_1)

    draw_ellipse(x_hat_2, gamma_2, 0.99, ax, 'green')

    x_hat_3, gamma_3 = kalman(x_hat_2, gamma_2, u[0], y[2], gamma_alpha_matrix,
                              gamma_beta_2, a_matrix, c_matrix_2)

    draw_ellipse(x_hat_3, gamma_3, 0.99, ax, 'blue')

    # ===========
    # Question 3
    # ===========
    # in 7.7_ex_three_equations.py we had
    x_hat = array([[1.31110605],
                   [1.75554201]]
                  )
    # so if we compare x_hat_3 with x_hat
    print(norm(x_hat_3 - x_hat))  # << 1 which is satisfying.
