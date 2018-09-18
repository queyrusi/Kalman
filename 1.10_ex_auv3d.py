#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""1.10_ex_auv3d.py

Slight adaptation of Pr. L. Jaulin's "rob exo 1.10 : 3D robot graphics",

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
dt = 0.05
fig = figure()
ax = Axes3D(fig)


def draw(x):
    """Plot of the UAV after rotation.

    Args:
        x (array): state vector of form

                    /  p_x  \
                    |  p_y  |
                    |  p_z  |
                    |   v   |
                    |  psi  |
                    | theta |
                    \  phi  /

    Returns:
        None
        
    """
    x = x.flatten()
    ax.clear()
    ax.set_xlim3d(-20, 20)
    ax.set_ylim3d(-20, 20)
    ax.set_zlim3d(0, 40)
    # --------------------
    # rotation matrix is :
    # --------------------
    e_mat = euler_matrix(x[4], x[5], x[6])
    # -------------------------------------------------
    # homogeneous rotation matrix is written as follow:
    # -------------------------------------------------
    r_mat = zeros((4, 4))
    for i in range(3):
        for j in range(3):
            r_mat[i][j] = e_mat[i][j]
    r_mat[3][:] = [0, 0, 0, 1]
    for i in range(3):
        r_mat[i][3] = x[i]
    # ---------------------
    # let's draw the plane:
    # ---------------------
    m_mat = array([[0, 0, 10, 0, 0, 10, 0, 0],
                   [- 1, 1, 0, - 1, - 0.2, 0, 0.2, 1],
                   [0, 0, 0, 0, 1, 0, 1, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1]
                   ]
                  )
    # We then rotate the plane:
    m_mat = r_mat @ m_mat
    # -------------------------------------------
    ax.plot(m_mat[0], m_mat[1], m_mat[2], color='blue')
    ax.plot(m_mat[0], m_mat[1], 0 * m_mat[2], color='black')
    ax.scatter(0, 0, 0, color='magenta')
    return


def euler_matrix(psi, theta, phi):
    """Rotation matrix for three rotations of psi, theta and phi about (1, 0, 0)
    (0, 1, 0) and (0, 0, 1) respectively.

    Args:
        psi (float):
        theta (float):
        phi (float):

    Returns:
        r (array): the Euler rotation matrix

    """

    nx = array([1, 0, 0])
    ny = array([0, 1, 0])
    nz = array([0, 0, 1])
    r = expm(psi * adjoint(nz)) @ expm(theta * adjoint(ny)) @ \
        expm(phi * adjoint(nx))
    return r


def f(x, u):
    """State vector for AUV system of form

                    /  p_x_dot  \
                    |  p_y_dot  |
                    |  p_z_dot  |
                    |   v_dot   |
                    |  psi_dot  |
                    | theta_dot |
                    \  phi_dot  /

    Returns:
        x_dot (array): time-differentiated state vector

    """
    # --------------------------------------------
    # from state vector we have:
    # --------------------------------------------
    v, psi, theta, phi = x[3], x[4], x[5], x[6]
    # --------------------------------------------
    x_dot = array([v * cos(theta) * cos(psi),
                   v * cos(theta) * sin(psi),
                   - v * sin(theta),
                   u[0],
                   sin(phi) / cos(theta) * v * u[1] +
                   cos(phi) / cos(theta) * v * u[2],
                   cos(phi) * v * u[1] - sin(phi) * v * u[2],
                   - 0.1 * sin(phi) * cos(theta) + tan(theta) * v *
                   (sin(phi) * u[1] + cos(phi) * u[2])
                   ]
                  )
    return x_dot


def dynamic_draw():
    """Draws UAV in motion with function draw.

    Returns:
        None

    """
    x = array([[0, 0, 10, 2, 0, 0, 0]]).T
    # print("MY X IS", x)
    # h_values = np.linspace(0, 1, number)
    for t in arange(0, 12, dt):
        print("initial shape is", x.shape)
        u = array([[2, 0, 0.1, 0]]).T
        # Euler method:
        # x = x + dt * f(x, u)
        # Runge Kutta method:
        x = x + dt * (0.25 * f(x, u) + 0.75 * f(x + (2 / 3) * dt * f(x, u), u))
        draw(x)
        pause(dt)
        t += 1  # absolutely useless, I just hate PEP8 remarks.
    return


if __name__ == "main":
    dynamic_draw()
    pause(1)
