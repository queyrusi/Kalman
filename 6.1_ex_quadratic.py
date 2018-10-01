#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""6.1_ex_quadratic.py

Code for Pr. L. Jaulin's "rob exo 6.1 : quadratique", youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    """f function

    Args:
        x:
        y:

    Returns:
        (value of f at (x, y))

    """
    return x * y


def draw_f():
    """draws f using matplotlib

    Returns:
        surf (mpl_toolkits.mplot3d.art3d.Poly3DCollection object):
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x_matrix = np.arange(-10, 11, 0.1)
    y_matrix = np.arange(-10, 11, 0.1)
    x_matrix, y_matrix = np.meshgrid(x_matrix, y_matrix)
    # print(x_matrix)
    u_matrix = x_matrix.copy()
    for i in range(x_matrix.shape[0]):
        for j in range(x_matrix.shape[0]):
            u_matrix[i][j] = f(x_matrix[i][j], y_matrix[i][j])
    surf = ax.plot_surface(x_matrix, y_matrix, u_matrix)

    plt.show()
    return surf


def draw_f_vector_field():
    """draws f gradient vector field

    Returns:
        (value of f at (x, y))
    """
    x_matrix = np.arange(-10, 10, 1)
    y_matrix = np.arange(-10, 10, 1)
    u_matrix, v_matrix = np.meshgrid(x_matrix, y_matrix)
    fig, ax = plt.subplots()
    q = ax.quiver(x_matrix, y_matrix, v_matrix, u_matrix)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10,
                 label='Quiver key, length = 10', labelpos='E')
    return


def g(x, y):
    """g function

    Args:
        x:
        y:

    Returns:

    """
    return 2 * x ** 2 + x * y + 4 * y ** 2 + y - x + 3


def draw_g():
    """draws g

    Returns:
        surf (mpl_toolkits.mplot3d.art3d.Poly3DCollection object):
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x_matrix = np.arange(-10, 11, 0.1)
    y_matrix = np.arange(-10, 11, 0.1)
    x_matrix, y_matrix = np.meshgrid(x_matrix, y_matrix)
    # print(x_matrix)
    u_matrix = x_matrix.copy()
    for i in range(x_matrix.shape[0]):
        for j in range(x_matrix.shape[0]):
            u_matrix[i][j] = g(x_matrix[i][j], y_matrix[i][j])
    surf = ax.plot_surface(x_matrix, y_matrix, u_matrix)

    plt.show()
    return surf


def draw_g_vector_field():
    """draws g gradient vector field

    Returns:

    """
    x_matrix = np.arange(-10, 10, 1)
    y_matrix = np.arange(-10, 10, 1)
    u_matrix, v_matrix = np.meshgrid(x_matrix, y_matrix)
    fig, ax = plt.subplots()
    new_u_matrix = u_matrix.copy()
    new_v_matrix = v_matrix.copy()
    for i in range(len(u_matrix)):
        for j in range(len(u_matrix[0])):
            new_u_matrix[i][j] = 4 * u_matrix[i][j] + v_matrix[i][j] - 1
            new_v_matrix[i][j] = u_matrix[i][j] + 8 * v_matrix[i][j] + 1
    q = ax.quiver(x_matrix, y_matrix, new_u_matrix, new_v_matrix)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10,
                 label='Quiver key, length = 10', labelpos='E')
    return
