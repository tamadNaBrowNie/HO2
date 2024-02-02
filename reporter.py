# type this in cmd frst : pip install mysql-connector-python
#basically install mysql-connecter for python
import mysql.connector as sql
def query(cursor,query):
    try:
        reply = cursor.execute(query)
        data = reply.fetchall()
        record = (','.join(row) for row in data)
        output = '\n'.join(record)
        return output
    except sql.Error as err:return str(err) #TODO: convert to proper error name
    finally: return 'smth broke'
def report(cursor):
    while True:
        reply = input('Generate report? [Y]es/[N]o').lower()
        if reply != 'y':break
        path = input('Save where?')
        name = input('Name it.')
        about = input('Describe it.')
        query = input('Query for it!') #TODO: Shawn, if they say this works, try to make an optimized query
        header = ':'.join(name,about)
        reply = query(cursor,query)
        report = '\n'.join(header,'Results:\n',query)
        print(report) #TODO: write to file instead
        with open(path, 'w') as f:
            f.write(report)
		
code = input('where config? 1 for default, 2 to create, 3 to load')
#TODO: make a working conf option
def enter():	
	param = ['user','password','host','port','database']
	args = [input(prompt) for prompt in param]
	return dict(zip(param,args))

def load():
    return {}
configs = {
1 :{},
2: enter(),
3:load()
}
config = configs[code]
try:
	db = sql.connect(**config)
	cursor = db.cursor()
	report(cursor)
except sql.Error as err:
    print(err)
#TODO: handle errors.
#TODO: include row lock then roll back


