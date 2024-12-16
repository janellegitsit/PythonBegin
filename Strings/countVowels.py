import sys

def vowels():
    string = sys.argv[1].lower()
    all_vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_in = set()
    for i in string:
        if i in all_vowels:
            vowel_in.add(i)
    print(len(vowel_in))

vowels()
