# type this in cmd frst : pip install mysql-connector-python
#basically install mysql-connecter for python
import mysql.connector as sql
import sys
import csv
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
def report(cursor):
    while True:
        reply = input('Generate report? [Y]es/[N]o: ').lower()
        if reply != 'y':break
        name = input('Name it. ')
        about = input('Describe it. ')
        query = input('Query for it! ') #TODO: Shawn, if they say this works, try to make an optimized query
        header = ':'.join((name,about))
        reply = access(cursor,query)
        report = '\n'.join((header,'Results:\n',reply))
        sys.stdout.write(report) #TODO: write to file instead
        toSave = input('Save to file? [Y]es/[N]o: ').lower()
        if toSave == 'y':save(report)
            
		
code = input('where config? 1 to create, 2 to load\n')
param = ['user','password','host','port','database']
def enter():	
	
	args = [input(f'{prompt}: ') for prompt in param]
	return dict(zip(param,args))

def load():
    conf = {}
    with open(input('Where file')) as f:

        for line in f:
            (key, val) = line.split(':')
            conf[key] = val.rstrip()
        print (conf)
    return conf
configs = {
'1':enter,
'2':load
}
config = configs[code]()
msg = 'fin'
try:
	db = sql.connect(**config)
	sys.stdout.write(f'welcome {config["user"] }')
	cursor = db.cursor()
	report(cursor)
except sql.Error as err: msg = str(err)
except KeyError: msg = f' {code} is an invalid input'
finally:sys.stdout.write(msg) 
#TODO: handle errors.
#TODO: include row lock then roll back


