import sys
def inrange(int_arg):
    div_num = []
    for num in range(1, 1000):
        if num % (int_arg**2) == 0 and num % (int_arg+7) == 0 and num % int_arg == 0:
            div_num.append(num)
    print(div_num)
inrange(int(sys.argv[1]))