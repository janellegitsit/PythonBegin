import sys
import numpy as np
def rly_ran():
    np.random.seed(42)
    ar_sz = sys.argv[1]
    int_sz = []
    if "," in ar_sz:
        int_sz.extend(map(int, ar_sz.split(",")))
    else:
        int_sz.append(int(ar_sz))
    array = np.random.randint(0, 10, int_sz)
    mult_int = int(sys.argv[2])
    mult_arr = array*mult_int
    index_int = int(sys.argv[3])
    if index_int > mult_arr.size:
        return
    else:
        print(f"Your random value is {mult_arr[index_int]}")


rly_ran()