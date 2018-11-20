#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.17_ex_invpend.py

Code for Pr. L. Jaulin's "rob exo 7.17 : kalman pendule inversé",
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
import scipy.signal


def draw_invpend(a, theta, pw, pax):  # inverted pendulum
    """

    Args:
        a:
        theta:
        pw:
        pax:

    Returns:

    """
    draw_box(a - 0.7, a + 0.7, -0.25, 0, pax, 'blue')
    plot([a, a - sin(theta)], [0, cos(theta)], 'magenta', linewidth=2)
    plot(pw, 0, 'ro')


def f(px, pu):
    """

    Args:
        px:
        pu:

    Returns:

    """
    a, theta, da, dtheta = px[0, 0], px[1, 0], px[2, 0], px[3, 0]
    dda = (m * sin(theta) * (g * cos(theta) - l * dtheta ** 2) + pu) / \
          (M + m * sin(theta) ** 2)
    ddtheta = (sin(theta) * ((m + M) * g - m * l * dtheta ** 2 * cos(theta)) +
               cos(theta) * pu) / (
                l * (M + m * sin(theta) ** 2))
    return array([[da], [dtheta], [dda], [ddtheta]])


if __name__ == "main":
    # ===========
    # Question 2
    # ===========

    # ax = init_figure(-3, 3, -3, 3)
    # M, l, g, m = 5, 1, 9.81, 1
    # dt = 0.1
    #
    # x = array([[0, 0.2, 0, 0]]).T
    # gamma_alpha = 0.00001 * eye(4)
    # A = array([[0, 0, 1, 0],
    #            [0, 0, 0, 1],
    #            [0, m*g/M, 0, 0],
    #            [0, (M+m)*g/(l*M), 0, 0]]
    #           )
    # B = array([[0, 0, 1/M, 1/(l*M)]]).transpose()
    # K = scipy.signal.place_poles(A, B, [-2, -2.1, -2.2, -2.3])
    # K = K.gain_matrix
    # E = array([[1, 0, 0, 0]])
    # h = - inv(E @ inv(A - B @ K) @ B)
    # for t in arange(0, 10, dt):
    #     clear(ax)
    #     w = 2
    #     draw_invpend(x[0, 0], x[1, 0], w, ax)
    #     u =  - K @ x + h * w
    #     α = mvnrnd1(gamma_alpha)
    #     x = x + dt * f(x, u) #+ α
    # pause(1)

    # ===========
    #
    # ===========

    # ax = init_figure(-3, 3, -3, 3)
    # M, l, g, m = 5, 1, 9.81, 1
    # dt = 0.1
    #
    # x = array([[0, 0.2, 0, 0]]).T
    # gamma_alpha = 0.00001 * eye(4)
    # A = array([[0, 0, 1, 0],
    #            [0, 0, 0, 1],
    #            [0, m*g/M, 0, 0],
    #            [0, (M+m)*g/(l*M), 0, 0]]
    #           )
    # B = array([[0, 0, 1/M, 1/(l*M)]]).transpose()
    # K = scipy.signal.place_poles(A, B, [-2, -2.1, -2.2, -2.3])
    # K = K.gain_matrix
    # E = array([[1, 0, 0, 0]])
    # C = array([[1, 0, 0, 0],
    #            [0, 1, 0, 0]])
    # L = scipy.signal.place_poles(A.T, C.T, [-2, -2.1, -2.2, -2.3]
    #                              ).gain_matrix.T
    # h = - inv(E @ inv(A - B @ K) @ B)
    # xhat = array([[0, 0, 0, 0]]).T
    # for t in arange(0, 10, dt):
    #     clear(ax)
    #     w = 1
    #     y = C @ x
    #     draw_invpend(x[0, 0], x[1, 0], w, ax)
    #     u =  - K @ xhat + h * w
    #     xhat = xhat + (A @ xhat + B @ u - L @ (C @ xhat - y)) * dt
    #     α = mvnrnd1(gamma_alpha)
    #     x = x + dt * f(x, u) #+ α
    # pause(1)

    # ===============
    # Question 4 & 5
    # ===============

    # ax = init_figure(-3, 3, -3, 3)
    # M, l, g, m = 5, 1, 9.81, 1
    # dt = 0.1
    #
    # x = array([[0, 0.2, 0, 0]]).T
    # A = array([[0, 0, 1, 0],
    #            [0, 0, 0, 1],
    #            [0, m*g/M, 0, 0],
    #            [0, (M+m)*g/(l*M), 0, 0]]
    #           )
    # B = array([[0, 0, 1/M, 1/(l*M)]]).transpose()
    # K = scipy.signal.place_poles(A, B, [-2, -2.1, -2.2, -2.3])
    # K = K.gain_matrix
    # E = array([[1, 0, 0, 0]])
    # C = array([[1, 0, 0, 0],
    #            [0, 1, 0, 0]])
    # L = scipy.signal.place_poles(A.T, C.T, [-2, -2.1, -2.2, -2.3]).gain_matrix.T
    # h = - inv(E @ inv(A - B @ K) @ B)
    # xhat = array([[0, 0, 0, 0]]).T
    # Qx = eye(4, 4)
    # Qalpha = dt * 0.00001 * eye(4, 4)
    # Qbeta = 0.01 ** 2 * eye(2, 2)
    #
    # for t in arange(0, 10, dt):
    #     clear(ax)
    #     w = 1
    #     y = C @ x + 0.01 * randn(2, 1)
    #     draw_invpend(x[0, 0], x[1, 0], w, ax)
    #     u = - K @ xhat + h * w
    #     # xhat = xhat + (A @ xhat + B @ u - L @ (C @ xhat - y)) * dt
    #     xhat, Qx = kalman(xhat, Qx, dt * B * u, y, Qalpha, Qbeta,
    #                       eye(4, 4) + dt * A, C)
    #     x = x + dt * f(x, u)
    # pause(1)
