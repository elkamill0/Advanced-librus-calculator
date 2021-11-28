from setup import open_file
from setup import write

def add_remove_grade(add_or_remove, subject, grade, weight):
    if (isinstance(grade, float) or isinstance(grade, int)) and isinstance(weight, int):
        data = open_file('experimental.json')
        for i in data:
            if i == subject:
                if add_or_remove:
                    data[subject].append([grade,weight])
                else:
                    data[subject].remove([grade, weight])
                write('experimental.json', subject, data[subject])
                return 0
        print("subject not found...")
        return 0
    else:
        print("grade and weight must be integer")