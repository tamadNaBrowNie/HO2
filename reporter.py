import mysql.connector as sql


#TODO: make a conf option

args = []
param = ['user','password','host','port','database']
for prompt in param:
	args.append(input(prompt))
config =dict(zip(param,args))
try:
	db = sql.connect(**config)
	cursor = db.cursor()

except sql.Error as err:
#TODO: handle errors.
	pass
#TODO: include row lock then roll back


