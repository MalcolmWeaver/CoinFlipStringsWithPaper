import numpy as np
import random


def create_correlation(str1, str2):
    assert (len(str1) == len(str2))
    length = len(str1)
    corr = [0] * length
    for idx in range(length):
        if str1[idx:] == str2[:length - idx]:
            corr[idx] = 1
    print(corr)
    return corr[1:]


def main():
    Xstr = input("X string")
    Ystr = input("Y string")
    print("Autocorrelation of X")
    create_correlation(Xstr, Xstr)
    print("Autocorrelation of Y")
    create_correlation(Ystr, Ystr)
    print("Correlation of X and Y")
    create_correlation(Xstr, Ystr)
    print("Correlation of Y and X")
    create_correlation(Ystr, Xstr)

main()
