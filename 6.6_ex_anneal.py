#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""6.6_ex_anneal.py

Slight adaptation from Pr. L. Jaulin's "rob exo 6.6 : recuit", youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey, L. Jaulin"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Development"
__name__ = "main"

from roblib import *


# -------
# config
# -------
A = array([[0, 7, 7, 9, 9, 7, 7, 4, 2, 0, 5, 6, 6, 5],
           [0, 0, 2, 2, 4, 4, 7, 7, 5, 5, 2, 2, 3, 3]])
B = array([[7, 7, 9, 9, 7, 7, 4, 2, 0, 0, 6, 6, 5, 5],
           [0, 2, 2, 4, 4, 7, 7, 5, 5, 0, 2, 3, 3, 2]])


def draw_room():
    """drawing obstacles

    """
    for j in range(A.shape[1]):
        plot(array([A[0, j], B[0, j]]), array([A[1, j], B[1, j]]), color='blue')


def draw(p, y, col):
    """

    Args:
        p (array): position vector
        y (array): distance vector
        col:

    Returns:

    """
    ax = init_figure(-2, 10, -2, 10)
    clear(ax)
    draw_room()
    draw_tank(p, 'darkblue', 0.1)
    p = p.flatten()
    y = y.flatten()
    for i in arange(0, 8):
        plot(p[0] + array([0, y[i] * cos(p[2] + i * pi / 4)]),
             p[1] + array([0, y[i] * sin(p[2] + i * pi / 4)]), color=col)


def f(p):
    """computes distances-to-the-walls vector

    Args:
        p:

    Returns:
        (array):

    """
    y_dyn = 8 * [9999999]
    # somehow, y_dyn[i] = x doesn't replace y_dyn[i] with floating value.
    # Had to replace it with a list and convert it to an array at the end.
    # ------------------
    for i in range(8):  # for every laser on the boat:
        u = array([cos(p[2][0] + (pi / 4) * i),
                   sin(p[2][0] + (pi / 4) * i)]
                  )
        u = u.transpose()
        m = array([p[0][0], p[1][0]])  # x, y center position vector
        for j in range(A[0].size):  # for each obstacle:
            a = A[:, j]  # end "a" of an obstacle segment
            b = B[:, j]  # end "b" of an obstacle segment
            vect1 = a - m
            vect2 = b - m
            vect3 = b - a
            if det([vect1, u]) * det([vect2, u]) <= 0:
                alpha = det([vect1, vect3]) / det([u, vect3])
                if alpha >= 0:
                    minimum = min(alpha, y_dyn[i])
                    y_dyn[i] = minimum
    return array(y_dyn)


def dynamic_draw():
    """draws every try of positioning the vehicle

    Returns:
        je (float): smallest norm difference

    Examples:
        >>>dynamic_draw()
        0.21570835585612996

    Note:
        Wait until the end for best result!

    """
    y = array([[6.4], [3.6], [2.3], [2.1], [1.7], [1.6], [3.0], [3.1]])
    y = y.transpose()
    t = 13
    p0 = array([[2], [1.5], [1]])  # initial guess
    # print("y est", y)
    # print("f(p0) est", f(p0))
    j0 = norm(y - f(p0))
    je = 0
    # ---------------------------
    while t > 0.01:
        rand_vect = rand(3, 1)
        pe = p0 + t * rand_vect
        # print("pe est", pe)
        # print("j0 est", j0)
        # print("y est", f(pe))
        je = norm(y - f(pe))
        # print("norme je est", je)
        draw(pe, y, 'red')
        if je < j0:
            j0 = je
            p0 = pe
        t = 0.98 * t
        # print("t vaut", t)
    return je


if __name__ == 'main':
    dynamic_draw()
