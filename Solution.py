#!/bin/python

from __future__ import print_function

import os
import sys

# Complete the solve function below.
def solve(a, m):
    if m == 2 or a == 0:
        return "YES"
    elif pow(a,(m-1)/2,m) == 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        am = raw_input().split()

        a = int(am[0])

        m = int(am[1])

        result = solve(a, m)

        fptr.write(result + '\n')

    fptr.close()
