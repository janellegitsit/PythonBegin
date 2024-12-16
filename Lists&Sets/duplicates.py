import sys
def dup():
    words = sys.argv[1:]
    un_word = sorted(set(words), reverse=True)
    print(un_word)    
dup()