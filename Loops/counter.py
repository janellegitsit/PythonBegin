import sys
def counter():
    abc_counted = {}
    str = input('blah')
    for a in str:
        abc_counter = 0
        for b in str:
            if b == a:
                abc_counter += 1
        if a not in abc_counted:   
            abc_counted[a] = abc_counter
    print(abc_counted)

counter()