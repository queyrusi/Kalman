#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.20_ex_radar.py

Code for Pr. L. Jaulin's "rob exo 7.20 : locboat",
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


def g(px):
    g1 = norm(px[::2, :] - a) ** 2
    g2 = norm(px[::2, :] - b) ** 2
    return array([[g1], [g2]])


dt = 0.02
gamma_alpha = diag([0, dt, 0, dt])
gamma_beta = eye(2)
x = array([[4], [0], [2], [0]])
a = array([[0, 0]]).T
b = array([[1, 0]]).T
Ak = array([[1, dt, 0, 0], [0, 1 - dt, 0, 0], [0, 0, 1, dt], [0, 0, 0, 1 - dt]])

if __name__ == "main":
    # ===========
    # Question 1
    # ===========

    # dt = 0.01
    # gamma_alpha = diag([0, dt, 0, dt])
    # gamma_beta = eye(2)
    # x = array([[4], [10], [10], [0]])
    # a = array([[0, 0]]).T
    # b = array([[1, 0]]).T
    # Ak = array(
    #     [[1, dt, 0, 0], [0, 1 - 0.01*dt, 0, 0], [0, 0, 1, dt],
    #      [0, 0, 0, 1 - 0.01*dt]])
    #
    # ax = init_figure(-20, 20, -20, 20)
    # for t in arange(0, 1, dt):
    #     clear(ax)
    #     plot(x[0], x[1], 'ro')
    #     alpha = mvnrnd1(gamma_alpha)
    #     x = Ak @ x + alpha

    # ===========
    # Question 2
    # ===========

    # dt = 0.02
    # gamma_alpha = diag([0, dt, 0, dt])
    # gamma_beta = eye(2)
    # x = array([[4], [0], [2], [0]])
    # a = array([[0, 0]]).T
    # b = array([[1, 0]]).T
    # Ak = array(
    #     [[1, dt, 0, 0], [0, 1 - dt, 0, 0], [0, 0, 1, dt], [0, 0, 0, 1 - dt]])
    #
    # ax = init_figure(-5, 5, -5, 5)
    # for t in arange(0, 1, dt):
    #     clear(ax)
    #     y = g(x) + mvnrnd1(gamma_beta)
    #     uk = array([[0]] * 4)
    #     plot(a[0], a[1], 'o')
    #     plot(b[0], b[1], 'o')
    #     plot(x[0, 0], x[2, 0], 'o')
    #     draw_disk(a, sqrt(y[0, 0]), ax, [0.8, 0.8, 0.8])
    #     draw_disk(b, sqrt(y[1, 0]), ax, [0.8, 0.8, 0.8])
    #     x = Ak @ x + mvnrnd1(gamma_alpha)
    # pause(1)

    # ===========
    # Question 4
    # ===========

    dt = 0.01
    gamma_alpha = diag([0, dt, 0, dt])
    gamma_beta = 25 * eye(2)
    x = array([[4], [1], [10], [0]])
    xhat = array([[0, 0, 1, 0]]).T
    gamma_x = 1e4 * eye(4)
    a = array([[0, 0]]).T
    b = array([[10, 0]]).T
    Ak = array([[1, dt, 0, 0],
                [0, 1 - 0.001*dt, 0, 0],
                [0, 0, 1, dt],
                [0, 0, 0, 1 - 0.001*dt]]
               )

    ax = init_figure(-10, 30, -20, 20)
    for t in arange(0, 1, dt):
        clear(ax)
        y = g(x) + mvnrnd1(gamma_beta)
        uk = array([[0]] * 4)
        plot(a[0], a[1], 'bo')
        plot(b[0], b[1], 'go')
        plot(x[0, 0], x[2, 0], 'ro')
        draw_disk(a, sqrt(y[0, 0]), ax, [0.8, 0.8, 0.8])
        draw_disk(b, sqrt(y[1, 0]), ax, [0.8, 0.8, 0.8])
        Ck = 2 * array([[xhat[0, 0] - a[0, 0], 0, xhat[2, 0] - a[1, 0], 0],
                        [xhat[0, 0] - b[0, 0], 0, xhat[2, 0] - b[1, 0], 0]]
                       )
        z = y - g(xhat) + Ck @ xhat
        xhat, gamma_x = kalman(xhat, gamma_x, 0, z, gamma_alpha, gamma_beta,
                               Ak, Ck)
        draw_ellipse(array([[xhat[0][0]], [xhat[2][0]]]),
                     array([[gamma_x[0][0], gamma_x[0][2]],
                            [gamma_x[2][0], gamma_x[2][2]]]
                           ),
                     0.99, ax, 'magenta')
        x = Ak @ x + mvnrnd1(gamma_alpha)
    pause(1)
