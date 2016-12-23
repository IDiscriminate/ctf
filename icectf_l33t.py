#!/usr/bin/python

import socket
import base64
import os
import time

host = 'l33tcrypt.vuln.icec.tf'
port = 6001

def fourtwentyblazeitup(j, i, k):
	#print m
	
	print i
	m = 'l33tserver please' + 'a'*j + k + i + 'l33tserver please' + 'a'*j
	client = socket.socket()
	data = base64.b64encode(m) + '\n'
	client.connect((host, port))	
	client.recv(2048)
	client.recv(2048)
	client.send(data)
	#time.sleep(0.4)
	client.recv(2048)
	c = client.recv(2048)
	b = base64.b64decode(c.rstrip()).encode("hex")
	#print b
	print b[128:160]
	print b[288:320]
	if b =='': return '2'
	else:	
		if (b[128:160] == b[288:320]): 
			k = k + i
			return '0'
			#j = j - 1
		else: return '1'
		client.close()
	#else:
	#	return '1'
	#	k = k
	#	j = j
	#	client.close()
	#print k
	time.sleep(0.6) 
	#print b
if __name__ == '__main__':
	t = "{}_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	c = ''
	jj = 62
	k = ''
	while jj > 0:
		for i in t:
			c = fourtwentyblazeitup(jj, i, k)
			while c == '2':
				c = fourtwentyblazeitup(jj, i, k)
				#if d == '0':  
			if c == '0':	
				jj = jj - 1
				k = k + i
				print k
				break
	#tcp_client('u')
