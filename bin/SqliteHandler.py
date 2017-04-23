#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('am_db',isolation_level=None)

def logConnection():
	conn.execute("INSERT INTO connection_detection_log(type,timestamp) VALUES ('CONNECTED',CURRENT_TIMESTAMP)")
	conn.commit
	return

def checkTask( task_name ):
	cursor = conn.cursor()
	cursor.execute("SELECT id,name,last_executed,result FROM tasks WHERE name = ?"\
			,(task_name,))
	for id, name, last_executed, result  in cursor:
		print "id = ", id
		print "name = ", name
		print "last_executed = ",last_executed
		print "result = ",result
	return

def updateTask():
	return


def closeDatabase():
	conn.close()
	return



##TESTING##
#checkTask( "test" )
