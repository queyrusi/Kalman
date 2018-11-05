#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""7.11_ex_kalm3steps.py

Code for Pr. L. Jaulin's "rob exo 7.11 : Kalman 3 steps",
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

# --------------------------------------
# config (parameters for Kalman filter):
# --------------------------------------
c_matrices = [array([[4., 0.]]),
              array([[10., 1.]]),
              array([[10., 5.]]),
              array([[13., 5.]]),
              array([[15., 3.]])
              ]
gamma_alpha_0 = array([[0, 0],
                       [0, 0]]
                      )
gamma_beta_0 = array([[9.]])  # !! scalar
a_matrix = array([[1, 0],
                  [0, 1]]
                 )
u = zeros((2, 1))
y = [5, 10, 11, 14, 17]
x_0_minus1 = array([[1.],
                    [-1.]]
                   )
gamma_0_minus1 = array([[4, 0],
                        [0, 4]]
                       )


# /!\  /!\  /!\
# draw_ellipse function was modified slightly to allow display of unfilled
# ellipses
# /!\  /!\  /!\
def draw_ellipse(c,Γ,η,ax,col): # Gaussian confidence ellipse with artist
    #draw_ellipse(array([[1],[2]]),eye(2),0.9,ax,[1,0.8-0.3*i,0.8-0.3*i])
    if (norm(Γ)==0):
        Γ=Γ+0.001*eye(len(Γ[1,:]))
    A=sqrtm(-2*log(1-η)*Γ)
    w, v = eig(A)
    v1=array([[v[0,0]],[v[1,0]]])
    v2=array([[v[0,1]],[v[1,1]]])
    f1=A @ v1
    f2=A @ v2
    φ =  (arctan2(v1 [1,0],v1[0,0]))
    α=φ*180/3.14
    e = Ellipse(xy=c, width=2*norm(f1), height=2*norm(f2), angle=α, fill=False)

    e.set_clip_box(ax.bbox)
    e.set_alpha(0.7)
    e.set_facecolor(col)
    ax.add_artist(e)


def kalman_iteration():
    """Executes as many kalman filter steps as there are matrices in list
    c_matrices.

    Args:

    Returns:
        x_hat_k_k (array size (2, 1)): estimation of x1 and x2
        gamma_k_k (array size (2, 2)): associated covariance matrix

    """
    ax = init_figure(-10, 10, -10, 10)

    current_x_hat = x_0_minus1  # kalman filter output 1
    current_gamma_k = gamma_0_minus1  # kalman filter output 2
    draw_ellipse(current_x_hat, current_gamma_k, 0.9, ax, 'black')
    for k in range(len(c_matrices)):
        current_x_hat, current_gamma_k = kalman(current_x_hat,
                                                current_gamma_k,
                                                u,
                                                y[k],
                                                gamma_alpha_0,
                                                gamma_beta_0,
                                                a_matrix,
                                                c_matrices[k]
                                                )
        draw_ellipse(current_x_hat, current_gamma_k, 0.9, ax, 'black')

    return current_x_hat, current_gamma_k


if __name__ == "main":
    print(kalman_iteration())
