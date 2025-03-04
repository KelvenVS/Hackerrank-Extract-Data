#!/bin/python3

import math
import os
import random
import re
import sys

def sorted_key(arr,k):
    new_arr = sorted(arr,key=lambda row: row[k])
    for line in new_arr:
        print(' '.join(map(str, line)))

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sorted_key(arr,k)
