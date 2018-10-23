#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.01_ex_gauss.py

Code for Pr. L. Jaulin's "rob exo 7.1 : gaussienne",
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


def q(dx_one, dx_two, g):
    """quadratic function inside the exponential function

    Args:
        dx_one:
        dx_two:
        g:

    Returns:

    """
    shape = dx_one.shape[-1]
    z_array = zeros((shape, shape))
    for i in range(shape):
        for j in range(shape):
            dx1_scalar = dx_one[i][j]
            dx2_scalar = dx_two[i][j]
            z_array[i][j] = array([[dx1_scalar],
                                   [dx2_scalar]]
                                  ).transpose() @ inv(g) @ array([[dx1_scalar],
                                                                  [dx2_scalar]]
                                                                 )
    return z_array


def z(dx, g):
    """density function of a mesh of (x1, x2) vector

    Args:
        dx (list like):

        g (array):

    Returns:

    """
    print(type(dx))
    shape = dx[0].shape[-1]
    z_array = zeros((shape, shape))
    quadr_array = q(dx[0], dx[1], g)
    for i in range(shape):
        for j in range(shape):
            z_array[i][j] = 1 / (2 * pi * sqrt(det(g))) * \
                            exp(-0.5 * quadr_array[i][j])
    return z_array


if __name__ == "main":
    x1, x2 = meshgrid(arange(-10, 10, 0.1), arange(-10, 10, 0.1))
    x_bar = array([[1, 2]]).transpose()
    gamma_matrix = eye(2, 2)
    dx1 = x1 - x_bar[0]
    dx2 = x2 - x_bar[1]

    fig = figure()
    ax = Axes3D(fig)
    ax.plot_surface(x1, x2, z([dx1, dx2], gamma_matrix))
    fig = figure()
    contour(x1, x2, z([dx1, dx2], gamma_matrix))
    # -----------
    # Question 2
    # -----------
    a_matrix = array([[cos(pi/6), -sin(pi/6)],
                      [sin(pi/6), cos(pi/6)]]
                     ) @  array([[1, 0],
                                 [0, 3]]
                                )
    gamma_y_matrix = a_matrix @ gamma_matrix @ a_matrix.transpose()
    b = array([[2, -10]]).transpose()
    y_bar = a_matrix @ x_bar + b
    dy1 = x1 - y_bar[0]
    dy2 = x2 - y_bar[1]
    ax.plot_surface(x1, x2, z([dy1, dy2], gamma_y_matrix))
    contour(x1, x2, z([dy1, dy2], gamma_y_matrix))
