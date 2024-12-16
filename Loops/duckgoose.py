import sys
def ducks_only():
    input = sys.argv[1:]
    ducks = []
    for word in input:
        if word == 'goose':
            continue
        else:
            ducks.append(word)
    print(ducks)
ducks_only()