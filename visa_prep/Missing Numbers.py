#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#
from collections import Counter

def missingNumbers(arr, brr):
    # Write your code here
    arr_count = Counter(arr)
    brr_count = Counter(brr)
    missing = []
    for num in brr_count:
        if brr_count[num] > arr_count.get(num, 0):
            missing.append(num)
    missing.sort()
    
    return missing

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
