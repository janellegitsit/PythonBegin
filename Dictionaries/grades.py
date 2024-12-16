import sys

def grades():
    grade = {"Biology" : 80,
             "Physics" : 88,
             "Chemistry" : 98,
             "Math" : 89,
             "English" : 79,
             "Music" : 67,
             "History" : 68,
             "Art" : 53,
             "Economics" : 95,
             "Psychology": 88}
    all_but = []
    subject = sys.argv[1]
    for key in grade:
        if subject == key:
            continue
        else: 
            all_but.append(grade[key])
    print(round(sum(all_but) / (len(grade)-1),2))
grades() 

    
