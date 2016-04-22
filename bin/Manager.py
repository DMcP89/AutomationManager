#!/usr/bin/python

import Scanner
import SqliteHandler
import logging
import sched
import time
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("../conf/automation.ini")

def run():
	logging.basicConfig(filename='../log/manager.log',level=logging.DEBUG)
	logging.debug('Manager Start')
	s = sched.scheduler(time.time,time.sleep)
	s.enter(60,1,networkScan, (s, ))
	s.run()
	return


def networkScan( scheduler ):
	logging.info('Scanning Network')
	scan = Scanner.scanNetwork( mac=config.get('ScannerProperties','target'),
					 network=config.get('ScannerProperties','network'))
	if (scan == 1):
		SqliteHandler.logConnection()
		logging.info('Connection Logged')
	scheduler.enter(60,1,networkScan,(scheduler, ))
	return


def main():
	run()
	logging.debug('Manager End \n')
	return

main()
