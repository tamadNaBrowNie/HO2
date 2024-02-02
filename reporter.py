# type this in cmd frst : pip install mysql-connector-python
#basically install mysql-connecter for python
import mysql.connector as sql
import sys
def query(cursor,query):
    try:
        reply = cursor.execute(query)
        data = reply.fetchall()
        record = (row for row in data)
        output = '\n'.join(record)
        
    except sql.Error as err: output = str(err)
    #TODO: convert to proper error name
    finally: return output
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
        header = ':'.join(name,about)
        reply = query(cursor,query)
        report = '\n'.join((header,'Results:\n',query))
        sys.stdout.write(report) #TODO: write to file instead
        toSave = input('Save to file? [Y]es/[N]o: ').lower()
        if toSave == 'y':save(report)
            
		
code = input('where config? 1 to create, 2 to load\n')
#TODO: make a working conf option
def enter():	
	param = ['user','password','host','port','database']
	args = [input(f'{prompt}: ') for prompt in param]
	return dict(zip(param,args))

def load():
    return {}
configs = {
'1':enter(),
'2':load()
}
config = configs[code]
msg = 'fin'
try:
	db = sql.connect(**config)
	cursor = db.cursor()
	report(cursor)
except sql.Error as err: msg = str(err)
except KeyError: msg = f' {code} is an invalid input'
finally:sys.stdout.write(msg) 
#TODO: handle errors.
#TODO: include row lock then roll back


