##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-205IQ-tom.hermann
## File description:
## proba
##

from math import pi, exp, sqrt

def proba(mean, sd, x):
    a = 1 / (sd * sqrt(2 * pi))
    b = (x - mean) ** 2
    c = 2 * sd ** 2
    d = exp(-(b / c))
    return a * d

def integral(mean, sd, start, end):
    t = start
    res = 0
    step = 0.001
    while t < end:
        res += proba(mean, sd, t) * step + (proba(mean, sd, t + step) - proba(mean, sd, t)) * step / 2
        t += step
    return res * 100