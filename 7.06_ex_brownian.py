#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.03_ex_predicov.py

Code for Pr. L. Jaulin's "rob exo 7.6 : brownian",
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
import numpy as np

def simul(delta, sx, tmax):
    """

    Args:
        delta:
        sx:
        tmax:

    Returns:

    """
    t = np.arange(0, tmax, delta)
    # print(tmax)
    # print(t)
    kmax = len(t)
    x = sx * randn(1, kmax)
    y = np.array([[.0] * len(x[0])])
    # print(y)
    for k in range(kmax - 1):
        # print(x)
        # print(y.shape)
        y[0][k + 1] = y[0][k] + delta * x[0][k]
        # print("OHIAO",y[0][k + 1])
    # print("x", x)
    # print("y", y)
    return t, x[0], y[0]



def brownian():
    tmax = 10
    delta = 0.01
    ax = init_figure(0, tmax, -10, 10)
    for i in range(100):

        t, x, y = simul(delta, 1/sqrt(delta), tmax)
        # print(y)
        # plot(t, x, '*b')
        plot(t, y, '*r')


if __name__ == "main":
    tmax = 100
    ax = init_figure(0, tmax, -10, 10)
    brownian()
    # δ = 0.1
    # T = arange(0, tmax, δ)
    # kmax = size(T)
    # X = randn(1, kmax)
    # X = X.flatten()
    # plot(T, X, 'red')
    # pause(1)

