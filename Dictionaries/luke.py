import sys

def luke():

    relations = {"Darth Vader" : "father",
                "Leia" : "sister",
                "Han" : "brother in law",
                "R2D2" : "droid",
                "Rey": "Padawan",
                "Tatooine" : "homeworld"}
    
    key = sys.argv[1]
    if key == "Darth Vader":  
        print(f"No, I am your {relations [key]}")
    else: 
        print(f"Luke, I am your {relations[key]}")

luke()

