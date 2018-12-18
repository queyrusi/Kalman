#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""5.02_ex_lidar.py

Code for Pr. L. Jaulin's "rob exo 5.2 : hokuyo",
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
import numpy as np

D = loadcsv("lidar_data.csv")

# n = 10
#
# Y = D[:, 1]
# Y = Y.reshape((len(Y),1))
# X = D[:, 0].reshape((len(Y),1))
#
#
# for i in range(X.shape[0]//n):
#     Xi = X[i*n:(i+1)*n,:]
#     Yi = Y[i*n:(i+1)*n,:]
#     plot(Xi,Yi,color='black')
# pause(1)

if __name__ == "main":
    # ===========
    # Question 1
    # ===========
    # n = 300
    # alphav = pi/3
    # dv = 3
    # xi = randn(n, 1)
    # yi = (dv - cos(alphav) * xi) / sin(alphav)
    # yi += 0.1* randn(n, 1)
    # plot(xi, yi, '+')
    # A = vstack((xi.T, yi.T)).T
    # b = ones((n, 1))
    # p = inv((A.transpose() @ A)) @ A.transpose() @ b
    # d = 1 / norm(p)
    # alpha = arctan2(p[1], p[0])
    #
    # residual_vector = A @ p - b
    # residual_norm = norm(residual_vector)

    # ===========
    # Question 2
    # ===========
    # n = 500
    # alpha = pi / 3 + 0.1 * rand(n, 1) + 2 * pi * np.floor(1.1 * rand(n, 1))
    # alpha = alpha + np.floor(1.1 * rand(n, 1)) * 100 * randn(n, 1)
    # alpham = arctan2(median(sin(alpha)), median(cos(alpha)))
    # plot(cos(alpha), sin(alpha), '+')

    # ===========
    # Question 3
    # ===========
    #
    # --------------------------------------------------------------------------
    #    Sans fonction de désambiguation (c'est à dire dans un cas ou le poids
    # des mesure est linéaire selon la mesure), les outliers d'orientation
    # peuvent faire varier dangereusement la moyenne (si l'outlier est très
    # grand ou très petit). L'affectation d'un poids au travers de la fonction
    # de désambiguation f permet non seulement de regrouper les mesures par
    # paquets se regroupant autour de :
    #
    #                           alpha3m + k * pi
    #
    # mais aussi de diminuer le bruit généré par les outliers.
    # --------------------------------------------------------------------------
    #
    Y = D[:, 1]
    Y = Y.reshape((len(Y),1))
    X = D[:, 0].reshape((len(Y),1))


    for i in range(X.shape[0]//n):
        Xi = X[i*n:(i+1)*n,:]
        Yi = Y[i*n:(i+1)*n,:]
        plot(Xi,Yi,'+b')
    pause(1)

    d3 = list()
    alpha3 = list()
    for i in arange(0, len(D) - n, n):
        x2 = X[i: i+n]
        y2 = Y[i: i+n]
        A2 = vstack((x2.transpose(), y2.transpose())).transpose()
        b2 = ones((n, 1))
        p = inv((A2.transpose() @ A2)) @ A2.transpose() @ b2
        d2 = 1 / norm(p)
        alpha2 = arctan2(p[1], p[0])
        if norm(A2 @ p - b2) < 0.05:
            plot(x2, y2, 'ro')
            d3.append(d2)
            alpha3.append(alpha2[0])
    alpha3m = (1 / 4) * arctan2(median(sin(4 * array(alpha3))),
                                median(cos(4 * array(alpha3))))


    # ===============
    # Question 4 5 6
    # ===============
    for k in range(0, 3):
        alpha4 = k * pi / 2 + alpha3m
        for j in range(len(alpha3)):
            print("le cos vaut", cos(alpha3[j] - alpha4))
        I = [i for i in range(len(alpha3)) if cos(alpha3[i] - alpha4) > 0.9]
        print("I", I)
        d4 = median([d3[i] for i in I])
        print("d4",d4)
        w = d4 * array([[cos(alpha4)],
                        [sin(alpha4)]]
                       ) @ array([[1, 1]]) + array([[-sin(alpha4)],
                                                    [cos(alpha4)]]
                                                   ) @ array([[-10, 10]]
                                                             )
        print("w0", w[0])
        print("w1", w[1])
        plot(w[0], w[1], 'red')
