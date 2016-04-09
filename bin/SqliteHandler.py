#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('./db/am_db',isolation_level=None)

def logConnection():
	conn.execute("INSERT INTO connection_detection_log(type,timestamp) VALUES ('CONNECTED',CURRENT_TIMESTAMP)")
	conn.commit
	return

def closeDatabase():
	conn.close()
	return

