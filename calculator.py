from setup import open_file

def calc(tab_with_grades):
    t_grade = 0
    t_weight = 0
    for word in tab_with_grades:
        if isinstance(word[0], float) or isinstance(word[0], int):
            try:
                t_grade = t_grade + word[0] * word[1]
                t_weight = t_weight + word[1]
            except:
                pass
    try:
        return t_grade/t_weight
    except:
        return 0

def calc_more(tab_with_grades, subject):
    t_grade = 0
    t_weight = 0
    data = open_file('goal.json')
    goal = data[subject]
    for word in tab_with_grades:
        if isinstance(word[0], float) or isinstance(word[0], int):
            t_grade = t_grade + word[0] * word[1]
            t_weight = t_weight + word[1]
    print(f"actual average: {calc(tab_with_grades)}")
    print(f"average to reach: {goal}")
    print("-------------------------")
    data = open_file('settings.json')
    for b in range(1, int(data['how_many_grades'])+1):
        a = (goal * t_weight + goal * b - t_grade)/b
        print(f"weight: {b}, grade: {a}")


