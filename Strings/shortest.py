# import sys

# def shortest():
#     string = sys.argv[1]
#     words = string.split()
#     sh_word = words[0]

#     for word in words:
#         if len(word) < len(sh_word):
#             sh_word = word
#     print(f'The shortest word is {sh_word.upper()}')

# shortest()

import sys
import numpy as np

def arr_args():
    # Collect command-line arguments as strings and convert to integers in one step
    int_arg = np.array([int(x) for x in sys.argv[1:]])
    
    # Print the type of the NumPy array
    print(type(int_arg))
    
    # Print the product of the elements in the array
    print(np.prod(int_arg))

arr_args()