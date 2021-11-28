import json
from py_librus_api import Librus

def open_file(filename):
    f = open(filename, 'r', encoding="utf8")
    data = json.load(f)
    f.close()
    return data
def write(filename, key, value):
    data = open_file(filename)
    data[key] = value
    f = open(filename, 'w', encoding="utf8")
    json.dump(data, f, ensure_ascii=False)
    f.close()
    return data
def write_dict(filename, dict):
    f = open(filename, 'w', encoding="utf8")
    dumped = json.dumps(dict, ensure_ascii=False).encode('utf8')
    f.write(dumped.decode())
    f.close()
def login(login, password):
    librus = Librus()
    while not librus.logged_in:
        if not librus.login(login, password):
            print("Log in failed! Check your username and/or password!")

        else:
            write('data.json', 'login', login)
            write('data.json', 'password', password)
            print("Logged in successfully!")

