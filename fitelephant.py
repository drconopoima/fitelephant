"""
Author: Piotr A. Zolnierczuk (zolnierczukp at ornl dot gov)
Version: 1.0.0
Adapted & Maintained by: Luis Diaz [drconopoima](https://twitter.com/drconopoima)

Original by Piotr had to be adapted as it used a 5th parameter for the eye
Anybody knows the 5th parameter makes the elephant wiggle his trunk (TO-DO)!

Based on a paper by:
Drawing an elephant with four complex parameters
Jurgen Mayer, Khaled Khairy, and Jonathon Howard,
Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017
"""
import numpy as np
from matplotlib import pyplot as plt

# elephant parameters
p1 = 50 - 30j
p2 = 18 + 8j
p3 = 12 - 10j
p4 = -14 - 60j


def fourier(t, C):
    f = np.zeros(t.shape)
    A, B = C.real, C.imag
    for k in range(len(C)):
        f = f + A[k] * np.cos(k * t) + B[k] * np.sin(k * t)
    return f


def elephant(t, p1, p2, p3, p4):
    npar = 6
    Cx = np.zeros((npar,), dtype="complex")
    Cy = np.zeros((npar,), dtype="complex")

    Cx[1] = p1.real * 1j
    Cx[2] = p2.real * 1j
    Cx[3] = p3.real
    Cx[5] = p4.real

    Cy[1] = p4.imag + p1.imag * 1j
    Cy[2] = p2.imag * 1j
    Cy[3] = p3.imag * 1j

    x = fourier(t, Cx)
    y = fourier(t, Cy)

    return x, y


x, y = elephant(np.linspace(0, 2 * np.pi, 1000), p1, p2, p3, p4)
plt.plot(y, -x, ".")
plt.show()
