import sys
import numpy as np
import pandas as pd
def randdf():
    np.random.seed(56)
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    arr = np.random.randint(0, 100, size =(rows, cols))
    df = pd.DataFrame(arr)
    print(df)
randdf()

#better way to solve the problem
#rows, cols = map(int, sys.argv[1:3])  # Unpack and convert to integers
