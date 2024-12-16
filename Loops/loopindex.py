import sys 
def loopindex():
    str_in = input('Please enter any amount of integers, seperated by spaces: ')
    int_out = [int(num)for num in str_in.split()]
    for i in range(len(int_out)):
       int_out[i] += i
    print(int_out)          
loopindex()
