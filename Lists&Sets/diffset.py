import sys

def matching():
    list_a = sys.argv[1:]
    list_b = ['apple', 'banana', 'mango', 'orange']
    set_a = set(list_a)
    set_b = set(list_b)
    matches = set_a - set_b
    print(matches)
matching()