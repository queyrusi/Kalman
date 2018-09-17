#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""1.7_ex_schuler.py

Slight adaptation from L. Jaulin's "rob exo 1.7 : Schuler oscillations",
youtube.com

Roblib package function dot will be used alongside natural python array
multiplication operator @ without distinction

Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *

# -------
# config
# -------
x = array([[1], [0.2], [0], [0]])
r = 10
l1 = 1
l2 = (-r + sqrt(r ** 2 + 4 * (l1 * r - l1 ** 2))) / 2
g = 9.81
dt = 0.05


def f(px, pa=0):
    """Time differentiated state vector.

    Args:
        px:
        pa (float):

    Returns:
        x_dot (array):

    """
    x_vector = px.flatten()
    x_dot = array([[x_vector[2]],
                   [x_vector[3]],
                   [pa / r],
                   [(l2 - l1) / (l1 ** 2 + l2 ** 2) * 
                    (g * sin(x_vector[1]) - pa * cos(x_vector[1])) - a / r]
                   ]
                  )
    return x_dot


def draw(px):
    """

    Args:
        px:

    Returns:

    """
    draw_disk(array([[0], [0]]), r, ax, "grey")
    theta = px[0, 0]
    alpha = px[1, 0]
    rho = array([r * cos(theta), r * sin(theta)])
    beta = alpha + theta
    plot(array([rho[0], rho[0] - l1 * cos(beta)]), array([rho[1], rho[1] - l1 *
                                                          sin(beta)]), 'blue')
    plot(array([rho[0], rho[0] + l2 * cos(beta)]), array([rho[1], rho[1] + l2 *
                                                          sin(beta)]), 'red')


if __name__ == "main":
    ax = init_figure(-12, 12, -12, 12)
    for t in arange(0, 5, dt):
        clear(ax)
        draw(x)
        # a = randn()
        # More entertaining:
        a = 2
        # Euler method:
        # x = x + dt * f(x, a)
        # Runge Kutta method:
        x = x + dt * (0.25 * f(x, a) + 0.75 * f(x + (2 / 3) * dt * f(x, a), a))
