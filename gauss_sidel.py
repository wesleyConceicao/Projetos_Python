# -*- coding: utf-8 -*-
"""Gauss_sidel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_cLxcA3NmbvGuiinZLRH9jaRzJ9ps8Sy
"""

import numpy as np
x1 = 0
x2 = 0
x3 = 0
epsilon = 0.000001
convergiu = False

x_old = np.array([x1, x2, x3])

print('Resultados da Iteraçoes')
print(' k,    x1,    x2,    x3 ')
for k in range(1, 50):
    x1 = (500 + 2 * x2 + 3 * x3) / 17
    x2 = (200 + 5 * x1 + 2 * x3) / 21
    x3 = (30 + 5 * x1 + 5 * x2) / 22
    x = np.array([x1, x2, x3])

    dx = np.sqrt(np.dot(x - x_old, x - x_old))

    print("%d, %.4f, %.4f, %.4f" % (k, x1, x2, x3))
    if dx < epsilon:
        convergiu = True
        print('Convergiu!')
        break

    # assign the latest x value to the old value
    x_old = x
print(" ")
if not convergiu:
    print('Nao converge, increase the # of iterations')