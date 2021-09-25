##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-205IQ-tom.hermann
## File description:
## error
##

from src.constante import FAILURE
from sys import stderr

def print_usage():
    print("USAGE")
    print("\t./205IQ u s [IQ1] [IQ2]")
    print("DESCRIPTION")
    print("\tu\tmean")
    print("\ts\tstandard deviation")
    print("\tIQ1\tminimum IQ")
    print("\tIQ2\tmaximum IQ")

def error(argv):
    if (len(argv) <= 2 or len(argv) >= 6):
        print_usage()
        exit(FAILURE)
    for i in argv[1:]:
        try:
            float(i)
        except ValueError:
            print("{} must be an number".format(i), file=stderr)
            exit(FAILURE)
        if (float(i) < 0):
            print("{} must be positif".format(i), file=stderr)
            exit(FAILURE)
        if (float(i) > 200 and i != argv[2]):
            print("{} must be inferior to 200", file=stderr)
            exit(FAILURE)
    if (len(argv) == 5):
        if (float(argv[4]) < float(argv[3])):
            print("IQ2 must be superior to IQ1", file=stderr)
            exit(FAILURE)


