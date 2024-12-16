import sys
def comp():
    str_in = (sys.argv[1:])
    int_out = []
    for num in str_in:
        int_out.append(int(num))
    for num in range(len(int_out)):
        if int_out[num] % 3 == 0:
            int_out[num] = int_out[num]*10
    print(int_out)                
comp()