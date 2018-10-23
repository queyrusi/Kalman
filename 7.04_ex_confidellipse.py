#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.04_ex_confidelipse.py

Code for Pr. L. Jaulin's "rob exo 7.4 : correcteur",
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
import random as random
import matplotlib.pyplot as plt

if __name__ == "main":
    # -----------
    # Question 1
    # -----------
    n_p = 1000
    random_gauss_x = [random.gauss(0, 1) for k in range(n_p)]
    random_gauss_y = [random.gauss(0, 1) for i in range(n_p)]
    p_gauss_matrix = array([random_gauss_x, random_gauss_y])
    x_bar = array([[1, 2]]).transpose()
    gamma_x = array([[3, 1],
                     [1, 3]]
                    )
    # Following is cloud centered at x_bar with ellipse parameters gamma_x:
    new_p_gauss = x_bar * ones((1, n_p)) + sqrtm(gamma_x) @ p_gauss_matrix
    ax = init_figure(-10, 10, -10, 10)
    plot(new_p_gauss[0], new_p_gauss[1], '+b')
    draw_ellipse(x_bar, gamma_x, 0.99, ax, 'red')

    # Drawing orthogonal unbiased estimator given by
    #
    #               x1_hat = 1/3 * (1 + x2)
    #
    x2 = arange(-10, 10, 0.01)
    x1 = 1/3 * (1 + x2)
    plot(x1, x2)

    # Best estimation to find x1 given x2.

    # Same for x2_hat
    #
    #               x2_hat = 1/3 * (5 + x1)
    x1 = arange(-10, 10, 0.01)
    x2 = 1/3 * (5 + x1)
    plot(x1, x2)
    plt.legend(["nuage de point gaussien centré (1, 2)", "estimateur x1",
                "estimateur x2"])
