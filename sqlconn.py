import mysql.connector as sql
import sys
def access(cursor,query):
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        record = (str(row) for row in data)
        output = '\n'.join(record)
        return output
    except sql.Error as err: return str(err)
    except AttributeError: return "wtf?"
    #TODO: convert to proper error name
def save(report):
    path = input('Save where?')
    with open(path, 'w') as f:f.write(report)

		


def enter():	
	param = ['user','password','host','port','database']
	args = [input(f'{prompt}: ') for prompt in param]
	return dict(zip(param,args))

def load():
    conf = {}
    with open(input('File where? ')) as f:

        for line in f:
            (key, val) = line.split(':')
            conf[key] = val.rstrip()
        print (conf)
    return conf

def connect(config):
    msg = 'fin'
    try:
        db = sql.connect(**config)
        sys.stdout.write(f'welcome {config["user"] }')
        cursor = db.cursor()
        return cursor
    except sql.Error as err: msg = str(err)
    finally:sys.stdout.write(msg) 
    return None
