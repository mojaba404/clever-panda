from os.path import exists
from json import dumps, loads

def create_file(filename):
    if not exists(filename):
        fh = open(filename, 'x')
        fh.close()

create_file('welcome.json')
def write_file(value:dict,filename):
    f = open(filename, 'wt', encoding='utf-8')
    f.write(dumps(value))
    f.close()


def read_file(filename):
    f = open(filename, 'rt', encoding='utf-8')
    result = loads(f.read())
    f.close()
    return result
    
