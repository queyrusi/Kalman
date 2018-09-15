#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""1.11_ex_staubli.py

Slight adaptation from L. Jaulin's "rob exo 1.10 : Staubli", youtube.com

Roblib package function dot will be used alongside natural python array
multiplication operator @ without distinction

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"

from roblib import *
import numpy as np

# -------
# config:
# -------
fig = figure()
ax = Axes3D(fig)
dt = 0.2


def draw():
    """Calls draw_axis and draw_arm method to plot robot. Applies rotations and
    translation matrix.

    Returns:
        None

    """
    ax.clear()
    # triangle below:
    rot_matrix = eye(4, 4)
    draw_axis(rot_matrix)
    # moving parts:
    for j in range(len(alpha)):
        r_old = rot_matrix
        rot_matrix = rot_matrix  @ translation([0, 0, r[j]]) \
            @ translation([delta[j], 0, 0])\
            @ rotation([0, alpha[j], 0])
        draw_arm(r_old, rot_matrix)
        rot_matrix = rot_matrix  @ rotation([0, 0, q[j]])
        draw_axis(rot_matrix)
    pause(0.01)
    return


def test_draw():
    """Little test can't hurt anybody"""
    r1 = eye(4, 4)
    r2 = r1 @ translation([0, 1, 1]) @ rotation([0, 0, 0])
    draw_arm(r1, r2)


def test_draw2():
    """Original test"""
    ax.clear()
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 2)
    j = array([[0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0],
               [1, 1, 1, 1, 1]]
              )
    plot3D(ax, j, "black", 2)
    pause(0.01)


def dynamic_draw(little_time=dt):
    """Automatically draws staubli robot arm

    Args:
        little_time (float): time resolution

    Returns:
        None

    """
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 2)
    # ---------------------------------------------------------
    global alpha, q, r, delta, alpha_s, delta_s, qs, rs
    alpha_s = [0, pi / 2, 0, - pi / 2, - pi / 2, - pi / 2, 0]
    delta_s = [0, 0.5, 0, -0.1, - 0.3, -1, 0]
    qs = [0.3, 0.3, 0.3, 0, 1.5, 0.1, 1]
    rs = [1, 0.5, 1, 0.1, 1, 0.2, 0.2]
    r = [0 * elt for elt in rs]
    alpha = [0 * elt for elt in alpha_s]
    delta = [0 * elt for elt in delta_s]
    q = [0 * elt for elt in qs]
    # -------------------------------------
    number = int(1 / little_time)
    h_values = np.linspace(0, 1, number)
    for i in range(len(alpha_s)):
        for h in h_values:
            draw()
            r[i] = h * rs[i]
        for h in h_values:
            draw()
            delta[i] = h * delta_s[i]
        for h in h_values:
            draw()
            alpha[i] = h * alpha_s[i]
        for h in h_values:
            draw()
            q[i] = h * qs[i]
    return


def dynamic_rotation(little_time=dt):
    """Dynamic rotation plot

    Args:
        little_time:

    Returns:
        None

    """
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 2)
    # ---------------------------------------------------------
    global alpha, q, r, delta, alpha_s, delta_s, qs, rs
    alpha = [0, pi / 2, 0, - pi / 2, - pi / 2, - pi / 2, 0]
    delta = [0, 0.5, 0, -0.1, - 0.3, -1, 0]
    q = [0.3, 0.3, 0.3, 0, 1.5, 0.1, 1]
    r = [1, 0.5, 1, 0.1, 1, 0.2, 0.2]
    # -------------------------------------
    number = int(1 / little_time)
    h_values = np.linspace(0, 1, number)
    for i in range(len(alpha_s)):
        while len(h_values) > 0:
            draw()
            q[i] = q[i] + dt
            # values in h_values are not used, only
            # length matters:
            h_values = h_values[: -1]
    return


def draw_axis(rota):
    """Axis plot with rotation and translation

    Args:
        rota (array):

    Returns:
        None

    """
    ax.set_xlim3d(-4, 4)
    ax.set_ylim3d(-4, 4)
    ax.set_zlim3d(0, 4)
    a_x = rota @ array([[0, 1],
                        [0, 0],
                        [0, 0],
                        [1, 1]]
                       )
    a_x_associate = array([a_x[0],
                           a_x[1],
                           a_x[2]]
                          )

    a_y = rota @ array([[0, 0],
                       [0, 1],
                       [0, 0],
                       [1, 1]]
                       )
    a_y_associate = array([a_y[0],
                           a_y[1],
                           a_y[2]]
                          )
    a_z = rota @ array([[0, 0],
                        [0, 0],
                        [0, 1],
                        [1, 1]]
                       )
    a_z_associate = array([a_z[0],
                           a_z[1],
                           a_z[2]]
                          )
    plot3D(ax, a_x_associate, "red")
    plot3D(ax, a_y_associate, "green")
    plot3D(ax, a_z_associate, "blue")


def translation(v):
    """Makes translation matrix

    Args:
        v (list): vector alongside which translation is made

    Returns:
        t (array): translation matrix

    """
    t = eye(4, 4)
    for i in range(3):
        t[i][3] = v[i]
    return t


def rotation(omega):
    """Makes rotation matrix

    Args:
        omega (list): vector about which rotation is made

    Returns:
        rot (array): rotation matrix

    """
    a = array([[0, - omega[2], omega[1]],
               [omega[2], 0, - omega[0]],
               [- omega[1], omega[0], 0]]
              )
    rot = zeros((4, 4))
    for i in range(3):
        for j in range(3):
            rot[i][j] = expm(a)[i][j]
    rot[-1][-1] = 1
    return rot


def draw_arm(r1, r2):
    """Draws arm of staubli robot after lower triangle undergo r1 & r2 rotation

    Args:
        r1 (array):
        r2 (array):

    Returns:
        None

    """
    e = 0.1
    #  Lower triangle:
    j0 = array([[-e, 3*e, -e, -e],
                [-e, -e, 3*e, -e],
                [0, 0, 0, 0],
                [1, 1, 1, 1]]
               )
    # Triangles undergo rotation
    j1 = dot(r1, j0)
    j2 = dot(r2, j0)
    # first long line of prism:
    j_1st = array([[j1[0][0], j2[0][0]],  # x
                   [j1[1][0], j2[1][0]],  # y
                   [j1[2][0], j2[2][0]]]  # z
                  )
    # second line:
    j_2nd = array([[j1[0][1], j2[0][1]],  # x
                   [j1[1][1], j2[1][1]],  # y
                   [j1[2][1], j2[2][1]]]  # z
                  )
    # thrid line:
    j_3rd = array([[j1[0][2], j2[0][2]],  # x
                   [j1[1][2], j2[1][2]],  # y
                   [j1[2][2], j2[2][2]]]  # z
                  )
    # ---------------------------------------
    plot3D(ax, j1)
    plot3D(ax, j2)
    plot3D(ax, j_1st)
    plot3D(ax, j_2nd)
    plot3D(ax, j_3rd)
    return


if __name__ == "main":
    ax.clear()
    dynamic_draw(dt)
    # dynamic_rotation(dt)
    pause(1)
