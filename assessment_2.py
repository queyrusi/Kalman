#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""Assessment 2

Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Finished"
__name__ = "main"

from roblib import *

# --------------------------------------
# config (parameters for Kalman filter):
# --------------------------------------
c_matrix = array([[2, 3, 2],
                  [1, 5, -3],
                  [-3, -2, 1]]
                 )
c_matrix_4 = array([[2, 3, 2],
                    [1, 5, -3],
                    [-3, -2, 1],
                    [4, -1, 3]]
                   )
c_matrix_0 = array([[2, 3, 2]])
c_matrix_1 = array([[1, 5, -3]])
c_matrix_2 = array([[-3, -2, 1]])
c_matrix_3 = array([[4, -1, 3]])

y = array([[10, -25, -1]]).transpose()
y_vector_4 = array([[10, -25, -1, 29]]).transpose()

x0 = array([[0.],
            [0.],
            [0.]]
           )
a_matrix = eye(3)

gamma_alpha_matrix = zeros((3, 3))

gamma_0_matrix = array([[1000, 0, 0],
                        [0, 1000, 0],
                        [0, 0, 1000]]
                       )

gamma_beta_0 = array([[1]])
gamma_beta_1 = array([[1]])
gamma_beta_2 = array([[9]])
gamma_beta_3 = array([[9]])
gamma_beta = array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 9, 0],
                    [0, 0, 0, 9]]
                   )

u = array([[0]])


def classic_solve():
    """

    Returns:
        x (vector shape (3,1)):

    """
    est = inv(c_matrix) @ y
    return est


if __name__ == "main":
    # ==============
    # Question 1.a
    # ==============
    print("Résolution classique : \n")
    print(classic_solve())
    print("\n")
    # ==============
    # Question 1.b
    # ==============
    x_hat_1, gamma_1 = kalman(x0, gamma_0_matrix, u, y[0], gamma_alpha_matrix,
                              gamma_beta_0, a_matrix, c_matrix_0
                              )

    x_hat_2, gamma_2 = kalman(x_hat_1, gamma_1, u[0], y[1], gamma_alpha_matrix,
                              gamma_beta_1, a_matrix, c_matrix_1)

    x_hat_3, gamma_3 = kalman(x_hat_2, gamma_2, u[0], y[2], gamma_alpha_matrix,
                              gamma_beta_2, a_matrix, c_matrix_2)
    print("Avec Kalman itératif, (x, y, z) vaut"
          " :")
    print("\n")
    print(x_hat_3)
    print("\n")
    # ==============
    # Question 1.c
    # ==============
    print("On obtient une différence :")
    print("\n")
    print(classic_solve() - x_hat_3)  # assez similaire (err < 0.01)
    print("\n")
    # ==============
    # Question 2.a
    # ==============
    k = inv((c_matrix_4.transpose() @ c_matrix_4)) @ c_matrix_4.transpose()
    print("Avec moindres carrés, (x, y, z) vaut"
          " : \n")
    p_chap = k @ y_vector_4
    print(p_chap)  # p_chap
    print("\n")

    # ==============
    # Question 2.b
    # ==============
    print("Avec BLUE, on obtient : \n")

    p_bar = array([[0, 0, 0]]).transpose()

    y_bar = c_matrix_4 @ p_bar

    # innovation:
    y_tilde = y_vector_4 - c_matrix_4 @ p_bar

    gamma_y = c_matrix_4 @ gamma_0_matrix @ c_matrix_4.transpose() + gamma_beta

    k_matrix = gamma_0_matrix @ c_matrix_4.transpose() @ inv(gamma_y)
    # estimated parameters:
    p_hat = p_bar + k_matrix @ y_tilde
    gamma_epsilon = gamma_0_matrix - k_matrix @ c_matrix_4 @ gamma_0_matrix
    # ++++++++++++++++
    # pas en one shot:
    # ++++++++++++++++
    print("pas d'un seul coup :")
    print(p_hat)
    print("\n")
    # ++++++++++++++++
    # et en one shot :
    # ++++++++++++++++
    print("et d'un seul coup : ")
    p_hat_try, gamma_try = kalman(x0, gamma_0_matrix, zeros((3, 1)), y_vector_4,
                                  gamma_alpha_matrix, gamma_beta, a_matrix,
                                  c_matrix_4)
    print(p_hat_try)
    print("\n")
    # ==============
    # Question 2.c
    # ==============
    x_hat_1, gamma_1 = kalman(x0, gamma_0_matrix, u, y_vector_4[0],
                              gamma_alpha_matrix,
                              gamma_beta_0, a_matrix, c_matrix_0
                              )

    x_hat_2, gamma_2 = kalman(x_hat_1, gamma_1, u[0], y_vector_4[1],
                              gamma_alpha_matrix,
                              gamma_beta_1, a_matrix, c_matrix_1)

    x_hat_3, gamma_3 = kalman(x_hat_2, gamma_2, u[0], y_vector_4[2],
                              gamma_alpha_matrix,
                              gamma_beta_2, a_matrix, c_matrix_2)

    x_hat_4, gamma_4 = kalman(x_hat_3, gamma_3, u[0], y_vector_4[3],
                              gamma_alpha_matrix,
                              gamma_beta_3, a_matrix, c_matrix_3)
    print("Avec Kalman itératif, (x, y, z) vaut"
          " :\n")
    print(x_hat_4)
    print("\n")
    # ==============
    # Question 2.d
    # ==============
    # a - b
    print("les différences entre moindres carrés et BLUE (one shot) :\n")
    print(p_chap - p_hat)
    print("\n")
    print("même résultat pour moindres carrés et BLUE (NON one shot !!) :\n")
    print(p_chap - p_hat_try)
    print("\n")
    # a - c
    print("les différences entre moindres carrés et Kalman itératif :\n")
    print(p_chap - x_hat_4)
    print("\n")
    # b - c
    print("les différences entre BLUE et Kalman itératif :\n")
    print(p_hat - x_hat_4)
    print("\n")

    print("matrice de covariances pour BLUE (one shot) :\n")
    print(gamma_try)
    print("\n")
    print("matrice de covariances pour BLUE (NON one shot !!) :\n")
    print(gamma_epsilon)
    print("\n")
    print("matrice de covariances Kalamn itératif :\n")
    print(gamma_4)
    print("\n")
