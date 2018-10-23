#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.03_ex_predicov.py

Code for Pr. L. Jaulin's "rob exo 7.3 : matcov",
youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Development"
__name__ = "main"


from roblib import *
import random as random


def rotating_cloud_plot():
    """

    Returns:

    """
    random_gauss_x = [random.gauss(0, 1) for k in range(n_p)]
    random_gauss_y = [random.gauss(0, 1) for i in range(n_p)]
    p_gauss_matrix = array([random_gauss_x, random_gauss_y])
    ax = init_figure(-10, 10, -10, 10)
    a_matrix = array([[0, 1],
                      [-1, 0]]
                     )
    b = array([[2, 3]]).transpose()
    x_moy = array([[1, 2]]).transpose()
    gamma_x = array([[3, 1],
                     [1, 3]]
                    )
    dt = 0.01
    ad_matrix = eye(2, 2) + dt * a_matrix

    steps = int(1 / dt)
    for t in linspace(0, 10, steps):
        ud = dt * sin(t) * b
        p_gauss_matrix = ad_matrix @ p_gauss_matrix + ud * ones((1, n_p))
        gamma_x = ad_matrix @ gamma_x @ ad_matrix.transpose()
        # print("ud", ud)
        # print("produit", )
        x_moy = ad_matrix @ x_moy + ud
        # plot(p_gauss_matrix[0], p_gauss_matrix[1], '+b')
        draw_ellipse(x_moy, gamma_x, 0.9, ax, 'red')
        pause(0.0001)
    return


if __name__ == "main":
    # ===========
    # Question 1
    # ===========
    n_p = 10
    # random_x = [random.uniform(0, 2) for k in range(n_p)]
    # random_y = [random.uniform(0, 2) for i in range(n_p)]
    # p_matrix = array([random_x, random_y])
    # plot(p_matrix[0],p_matrix[1], '*k')

    random_gauss_x = [random.gauss(0, 1) for k in range(n_p)]
    random_gauss_y = [random.gauss(0, 1) for i in range(n_p)]
    p_gauss_matrix = array([random_gauss_x, random_gauss_y])
    # plot(p_gauss_matrix[0],p_gauss_matrix[1], '*k')

    x_bar = array([[1, 2]]).transpose()
    gamma_x = array([[3, 1],
                     [1, 3]]
                    )
    new_p_gauss = x_bar * ones((1, n_p)) + sqrtm(gamma_x) @ p_gauss_matrix
    ax = init_figure(-10, 10, -10, 10)
    # plot(new_p_gauss[0], new_p_gauss[1], '+b')
    # ===========
    # Question 2
    # ===========
    # draw_ellipse(x_bar, gamma_x, 0.9, ax, 'red')
    # draw_ellipse(x_bar, gamma_x, 0.99, ax, 'green')
    # draw_ellipse(x_bar, gamma_x, 0.999, ax, [1, 0.8, 0.8])
    # ===========
    # Question 3 ------ Non testé
    # ===========
    # mean1 = sum(p_gauss_matrix[0]) / len(p_gauss_matrix[0])
    # mean2 = sum(p_gauss_matrix[1]) / len(p_gauss_matrix[1])
    # x_bar_estimate = array([mean1, mean2]).transpose()
    # x_tilde = p_gauss_matrix - array([[mean1],
    #                                   [mean2]
    #                                  )
    # gamma_x_estimate = x_tilde @ x_tilde.transpose()
    # gamma_x_estimate = mean(gamma_x_estimate
    # ===========
    # Question 4
    # ===========
    rotating_cloud_plot()
    # ===========
    # Question 5
    # ===========
    # ...
