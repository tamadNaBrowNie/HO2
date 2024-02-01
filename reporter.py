from mysql.connector import connect
args = []
param = ['user','password','host','port','database']
for prompt in prompts:
	params.append(input(prompt))
config =dict(zip(param,args))
db = connect(**params)
cursor = db.cursor()

