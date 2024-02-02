# type this in cmd frst : pip install mysql-connector-python
#basically install mysql-connecter for python
import mysql.connector as sql
def query(cursor,query):
    try:
        reply = cursor.execute(query)
        data = reply.fetchall()
        for row in data: print (row)
        
    except sql.Error as err:print(err)
    # finally:
def report(cursor):

    while True:
        reply = input('Generate report? [Y]es/[N]o').lower()
        if reply != 'y':break
        name = input('Name it.')
        about = input('Describe it.')
        query = input('Query for it!') #TODO: Shawn, if they say this works, try to make an optimized query
        reply = query(cursor,query)
        
        

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

except sql.Error as err:
    print(err)
#TODO: handle errors.
#TODO: include row lock then roll back


