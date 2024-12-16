import sys
def capcut():
    string = sys.argv[1]
    capital = []
    sum_ind = 0
    index = 0
    for i in string:
        if i.isupper():
            capital.append(i)
    print(len(capital))
    for i in string:
        if i.isupper():
            sum_ind = sum_ind + index
        index += 1
    print(sum_ind)
capcut()