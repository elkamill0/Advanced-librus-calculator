try:
    from py_librus_api import Librus
except:
    from pip._internal import main as pip
    pip(['install', '--user', 'py_librus_api'])
    pip(['install', '--user', 'requests'])
    from py_librus_api import Librus
import setup
import calculator


def update_goal():
    d = {}
    data = setup.open_file('grades.json')
    pattern = [1.75, 2.75, 3.75, 4.75, 5.75, 6]
    for i in data:
        avg = calculator.calc(data[i])
        for gr in pattern:
            if gr >= avg:
                d[i] = gr
                break
    setup.write_dict('goal.json', d)

def main(login, password):
    librus = Librus()
    while not librus.logged_in:
        if not librus.login(login, password):
            print("Log in failed! Please check login and password and try again")
        else:
            print("Logged in Successfully!")
            grades = librus.get_grades()
            d = {}
            for i in grades:
                tab = []
                for a in grades[i]:
                    tab.append([parse_grade(a['Grade']), a['Weight']])
                d[i] = tab
            setup.write_dict('grades.json', d)
            print("Grades updated successfully!")
            update_goal()

def parse_grade(grade):
    if len(grade) == 2:
        if '+' in grade:
            final = int(grade[0]) + 0.5
        elif '-' in grade:
            final = int(grade[0]) - 0.25
        else:
            final = grade
    else:
        try:
            final = int(grade)
        except:
            final = grade
    return final