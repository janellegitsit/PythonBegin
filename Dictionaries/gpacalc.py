import sys
def gpa_calc():
    gpa_dict = {"A" : 4.00,
                "A-" : 3.66,
                "B+" : 3.33,
                "B" : 3.00,
                "B-" : 2.66,
                "C+" : 2.33,
                "C" : 2.00,
                "C-" : 1.66,
                "D+" : 1.33,
                "D" : 1.00,
                "D-" : 0.66,
                "F" : 0.00}
    user_gr = []
    grades = sys.argv[1:5]
    for i in grades: 
            user_gr.append(gpa_dict[i.upper()])
    print(f"My GPA is {sum(user_gr) / len(user_gr):.2f}")

gpa_calc()