#!/usr/bin/python

import nmap
import ConfigParser
import logging

config = ConfigParser.ConfigParser()

config.read("../conf/automation.ini")


def scanNetwork( mac, network ):
	logging.debug('Scanning network for '+mac)
	logging.debug('Network: '+network)
	results = 0
	nm = nmap.PortScanner()

	nm.scan(hosts= network, arguments= '-sP')
	host_list = nm.all_hosts()
	logging.debug('Host List')
	for host in host_list:
        	if  'mac' in nm[host]['addresses']:
                	logging.debug(host+' : '+nm[host]['addresses']['mac'])
                	if mac == nm[host]['addresses']['mac']:
                        	logging.debug('Target Found')
				
				results = 1
				return results


#test = scanNetwork('***REMOVED***')
#print test


                                                                          
