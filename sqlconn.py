import mysql.connector as sql
import sys
"""_summary_: query at database cursor. returns a string for the report. returns err as string if sql error. if cursor is inaccessible, raise AttributeError
"""
def report(cursor,query):
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        record = (','.join(row) for row in data)
        output = '\n'.join(record)
        return output
    except sql.Error as err: return str(err) #TODO: future maintainer, raise appropriate python equivalent
    except AttributeError: 
        raise (AttributeError)
    #TODO: convert to proper error name

    """
    connect to open mysql db using config. throws ValueError if config has invalid values
    """
def connect(config):
    msg = 'fin'
    try:
        db = sql.connect(**config)
        return db
    except sql.Error as err: 
        msg = str(err)
        raise(ValueError)
        
    finally:sys.stdout.write(msg) 
    return None
