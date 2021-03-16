import numpy as np
import random


def create_good_arr(instr):
    good_arr = []
    # array will have size of 1 + number of heads/tails
    for i in range(len(instr) + 1):
        good_arr.append(instr[:i])
    # print(good_arr)
    return good_arr


def create_close_arr(g_arr):
    close_arr = []
    for i in range(len(g_arr)):
        close_arr.append(g_arr[i][:-1])
        if g_arr[i] == "":
            close_arr[i] = ""
        elif g_arr[i][-1] == "H":
            close_arr[i] += "T"
        elif g_arr[i][-1] == "T":
            close_arr[i] += "H"
        else:
            print("Invalid string. WARINING: Anything from here on out is "
                  "undefined behavior.")
    # print(close_arr)
    return close_arr


def create_fall_backsarr(g_arr, c_arr):
    assert (len(g_arr) == len(c_arr))
    length = len(g_arr)
    fallback_arr = [0] * length
    # check for if a fail creates an earlier state. If so, this would influence
    # the markov chain
    for idx in range(length):
        for sub_idx in range(idx):
            if c_arr[idx].endswith(g_arr[sub_idx]):
                fallback_arr[idx] = sub_idx
    print("Very important FALLBACK ARRAY to talk about:")
    print(fallback_arr[1:])
    return fallback_arr[1:]


def matrix_setup(f_arr, length):
    matrix = np.identity(length)
    good_case_matrix = np.diagflat([1] * (length - 1), 1)  # you revert to
    # Xhhh from Xhh if you get a heads
    for idx in range(len(f_arr)):
        matrix[idx][f_arr[idx]] -= 0.5
    matrix = matrix - 0.5 * good_case_matrix
    print(matrix)
    # print("DETERMINANT of inverse is", 1/np.linalg.det(matrix)) # always
    # 2^-len(str)
    return matrix


def matrix_solve(matrix):
    matrix_inverse = np.linalg.inv(matrix)
    # I hope they all invert lol
    # print(matrix_inverse)
    ones = np.ones((matrix.shape[0], 1))
    # print(ones)
    answer = np.matmul(matrix_inverse, ones)
    return answer


def main():
    teststr = input("This machine calculates the expected number of flips "
                    "before you first see a particular series of HEADS and "
                    "TAILS given a fair coin. Input a string of 'H's and 'T's "
                    "(case sensitive).")

    g_arr = create_good_arr(teststr)
    c_arr = create_close_arr(g_arr)
    f_arr = create_fall_backsarr(g_arr, c_arr)
    matrix = matrix_setup(f_arr, len(teststr))
    answer = matrix_solve(matrix)
    print("The expected number of coin flips to get your string is as follows:")
    print(answer[0][0])
    # print("The full array of expected values follows:")
    # print(answer)


main()
