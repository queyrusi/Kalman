#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""6.4_ex_transfer.py

Code for Pr. L. Jaulin's "rob exo 6.4 : estimation d'une fonction de transfert",
youtube.com


Check https://github.com/queyrusi/Kalman for updates!

"""

__author__ = "Simonkey"
__credits__ = ["L. Jaulin"]
__version__ = "1.0.1"
__email__ = "simon.queyrut@ensta-bretagne.org"
__status__ = "Development"
__name__ = "main"

from roblib import *
import numpy as np

m = array([[1, 0, -1, 1],
           [2, 1, 1, -1],
           [-3, 2, -1, 1],
           [-7, -3, 1, -1],
           [-11, -7, -1, 1],
           [-16, -11, 1, -1]]
          )

j = (m.transpose() @ m)

# result is:

# array([[440, 270,  -8,   8],
#        [270, 184,  -8,   8],
#        [ -8,  -8,   6,  -6],
#        [  8,   8,  -6,   6]])

rank = np.linalg.matrix_rank(j)
print(rank)
# The matrix is of rank 3 != 4 so cannot be inversed.
