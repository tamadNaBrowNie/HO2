# Generate simple reports with this repo.
#TODO make it graphical ig
## sqlconn functions

### report
#### generate a report from db
@params 
cursor: db cursor <br>
@params 
query: mysql query to execute

### connect
#### connect to database on a running sql server
@params
config: dictionary whose k are the params of mysql.connector.connect and the v are the args to pass.

## reporter.py
#### sample of report generating script
