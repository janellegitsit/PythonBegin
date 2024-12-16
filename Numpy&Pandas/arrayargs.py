import sys
import numpy as np
def arr_args():
    string = sys.argv[1:]
    int_arg = []
    for x in string:
        int_arg.append(int(x))
    arr_arg = np.array(int_arg)
    print(type(arr_arg))
    print(np.prod(arr_arg))
arr_args()
