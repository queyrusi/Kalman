#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.16_ex_pendulum.py

Code for Pr. L. Jaulin's "rob exo 7.16 : pendulum",
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


def f(px, pu):
    """

    Args:
        px:
        pu:

    Returns:

    """
    px = px.flatten()
    pu = pu.flatten()
    return (array([[px[1]],
                   [- sin(x[0]) + pu[0]]]
                  )
            )


def draw(a, color, thick):
    """

    Args:
        a:
        color:
        thick:

    Returns:

    """
    plot(sin(a), -cos(a), 'o')
    # print(sin(a))
    plot([0, sin(a)], [0, -cos(a)], color, thick)


if __name__ == "main":
    ax = init_figure(-1.5, 1.5, -1.5, 1.5)
    x = array([[0, 0]]).transpose()
    xr = array([[0, 0]]).transpose()
    sigma_x = 0.05
    sigma_y = 0.1
    g_beta = sigma_y ** 2
    dt = 0.05
    C = array([[0, 1]])
    p_matrix = eye(2, 2)
    g_alpha = dt * sigma_x ** 2

    for t in arange(0, 15, dt):
        clear(ax)
        y = C @ x + sigma_y * randn()
        w, dw, ddw = sin(t), cos(t), - sin(t)

        covxr = 5 ** 2 * p_matrix[0][0]

        u = sin(xr[0][0]) + (w - xr[0][0]) + 2 * (dw - xr[1][0]) + ddw
        a_matrix = array([[1, dt],
                          [-dt * cos(xr[0]), 1]]
                         )
        v = dt * array([[0],
                        [-sin(xr[0]) + xr[0] * cos(xr[0]) + u]]
                       )
        xr, p_matrix = kalman(xr, p_matrix, v, y, g_alpha, g_beta, a_matrix, C)
        # dodo = f(x, u)

        draw(w, 'red', 2)
        draw(xr[0], 'green', 2)
        draw(x[0][0], 'black', 2)
        draw_arc(array([[0, 0]]).transpose(), array([[sin(xr[0] - covxr),
                                                      - cos(xr[0] - covxr)]]
                                                    ),
                 2 * covxr,
                 'magenta')
        print("xr", xr)
        x = x + dt * f(x, u) + sigma_x * sqrt(dt) * randn(2, 1)
