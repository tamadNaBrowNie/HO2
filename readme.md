sqlconn

report: generate a report from db
	@params 
	cursor: db cursor
		type: mysql-connector.cursor
	query: mysql query to execute
		type: string
	connect: connect to database on a running sql server
	@params
	config: dictionary whose k are the params of mysql.connector.connect and the v are the args to pass.
		type: dict
