#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-205IQ-tom.hermann
## File description:
## main
##

from sys import argv
from src.error import error
from src.calcule import density_function, percent_inf, percent_between
from src.constante import *

def main():
    error(argv)
    mean = float(argv[1])
    sd = float(argv[2])
    if (len(argv) == 3):
        density_function(mean, sd)
    elif (len(argv) == 4):
        percent_inf(mean, sd, int(argv[3]))
    elif (len(argv) == 5):
        percent_between(mean, sd, int(argv[3]), int(argv[4]))
    else:
        exit(FAILURE)
    exit(SUCCESS)

if __name__ == "__main__":
    main()