# type this in cmd frst : pip install mysql-connector-python
#basically install mysql-connecter for python

import sys
from sqlconn import *



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
configs = {
'1':enter,
'2':load
}
code = input('where config? 1 to create, 2 to load\n')
try:
    config = configs[code]()
    cursor = connect(config)
    report(cursor)
except KeyError: sys.stdout.write(f'{code} is an invalid input')
#TODO: handle errors.
#TODO: include row lock then roll back


