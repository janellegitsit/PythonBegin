import sys 
def palindrome():
    string = sys.argv[1].lower()
    rstring = []
    for i in string:
        if i.isalnum():
            rstring += i
    if rstring == rstring[::-1]:
        print("It's a palindrome!")
    elif rstring != rstring[::-1]: 
        print("It's not a palindrome!")
palindrome()
