##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-205IQ-tom.hermann
## File description:
## calcule
##

from src.proba import proba, integral

def density_function(mean, sd):
    for i in range(0, 201):
        res = proba(mean, sd, i)
        print("{} {:.5f}".format(i, res))

def percent_inf(mean, sd, lim):
    res = integral(mean, sd, 0, lim)
    print("{:.1f}% of people have an IQ inferior to {}".format(res, lim))

def percent_between(mean, sd, start, lim):
    res = integral(mean, sd, start, lim)
    print("{:.1f}% of people have an IQ between {} and {}".format(res, start, lim))

