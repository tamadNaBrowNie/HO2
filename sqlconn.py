import mysql.connector as sql
import sys
"""_summary_: query at database cursor. returns a string for the report. returns err as string if sql error. if cursor is inaccessible, returns a special string 
"""
def report(cursor,query):
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        record = (str(row) for row in data)
        output = '\n'.join(record)
        return output
    except sql.Error as err: return str(err)
    except AttributeError: return "wtf?"
    #TODO: convert to proper error name

def connect(config):
    msg = 'fin'
    try:
        db = sql.connect(**config)
        sys.stdout.write(f'welcome {config["user"] }')
        cursor = db.cursor()
        return cursor
    except sql.Error as err: msg = str(err)
    finally:sys.stdout.write(msg) 
    return None
