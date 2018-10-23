#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.02_ex_sixcov.py

Code for Pr. L. Jaulin's "rob exo 7.2 : ellipse de confiance", youtube.com

plot_cov_ellipse function adapted from
joferkington/oost_paper_code/error_ellipse.py

Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin", "joferkington"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def plot_cov_ellipse(cov, pos, ax=None):
    """
    Plots an `nstd` sigma error ellipse based on the specified covariance
    matrix (`cov`). Additional keyword arguments are passed on to the
    ellipse patch artist.
    Parameters
    ----------
        cov : The 2x2 covariance matrix to base the ellipse on
        pos : The location of the center of the ellipse. Expects a 2-element
            sequence of [x0, y0].
        ax : The axis that the ellipse will be plotted on. Defaults to the
            current axis.
        Additional keyword arguments are pass on to the ellipse patch.
    Returns
    -------
        A matplotlib ellipse artist
    """
    def eigsorted(covar):
        valus, vects = np.linalg.eigh(covar)
        order = valus.argsort()[::-1]
        return valus[order], vects[:, order]

    if ax is None:
        ax = plt.gca()

    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))

    # Width and height are "full" widths, not radius
    width = np.sqrt(vals[0])
    height = np.sqrt(abs(vals[1]))
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, fill=False)
    ellip.set_facecolor('b')
    ax.add_artist(ellip)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    ax.set_aspect('equal')
    plt.show()
    return ellip


if __name__ == "main":
    a1_matrix = array([[1, 0],
                       [0, 3]]
                      )
    a2_matrix = array([[cos(pi/4), -sin(pi/4)],
                       [sin(pi/4), cos(pi/4)]]
                      )
    g1 = eye(2, 2)
    g2 = 3 * eye(2, 2)
    g3 = a1_matrix @ g2 @ a1_matrix.transpose() + g1
    g4 = a2_matrix @ g3 @ a2_matrix.transpose()
    g5 = g4 + g3
    g6 = a2_matrix @ g5 @ a2_matrix.transpose()
    plot_cov_ellipse(g1, [0, 0], ax=None)
    plot_cov_ellipse(g2, [0, 0], ax=None)
    plot_cov_ellipse(g3, [0, 0], ax=None)
    plot_cov_ellipse(g4, [0, 0], ax=None)
    plot_cov_ellipse(g5, [0, 0], ax=None)
    plot_cov_ellipse(g6, [0, 0], ax=None)
    plt.show()
