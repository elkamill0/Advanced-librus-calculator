import sys
from load_grades import main
from calculator import calc_more
import calculator
from setup import open_file
from setup import write
import getpass
def help():
    print("""
    Provide arguments to calc your average grade
        main.py [argument]
        list of arguments:
            number_of_weight [number]  - set number of weight to calculate
            get_settings - printing settings file
            predict [subject] - predict grades to get of your average to reach goal average
            calc [subject] - calc your acutally average
            update - update your grades list from librus
            help - show help just like here     
            list - show subjects list""")

arg = sys.argv
if len(sys.argv) > 1:
    if arg[1] == "predict":
        data = open_file('grades.json')
        calc_more(data[arg[2]], arg[2])
    elif arg[1] == "calc":
        data = open_file('grades.json')
        print(calculator.calc(data[arg[2]]))
    elif arg[1] == "update":
        l = input("login: ")
        p = getpass.getpass("password (for safety it will be hidden): ")
        main(l, p)
    elif arg[1] == "list":
        data = open_file('grades.json')
        for i in data:
            print(i)
    elif arg[1] == "number_of_weight":
        try:
            x = float(arg[2])
            write('settings.json', "how_many_grades", float(arg[2]))
        except ValueError:
            print(f"Value error of argument: {arg[2]}")
        except:
            print("something went wrong")
    elif arg[1] == "get_settings":
        data = open_file('settings.json')
        print(data)
    elif arg[1] == "help":
        help()
    else:
        print("Unknown command. Try again or help")



else:
    print("""
    ---------------------------------------------------------
    |   WELCOME TO PROFESSIONAL LIBRUS GRADES CALCULATOR    |
    ---------------------------------------------------------""", end="")
    help()


