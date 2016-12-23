#!/usr/bin/python
#idis

import hashlib
import random 
import string


def fourtwentyblazeitup():
	c = 1
	while c == 1:
		s = string.lowercase + string.digits
		p = ''.join(random.sample(s,10))
		if hashlib.md5(p).hexdigest()[28:32] == '1337':
			print 'Found!!'
			print p
			print hashlib.md5(p).hexdigest()
			c = 0;
		else: 
			print hashlib.md5(p).hexdigest()[28:32] 
	
if __name__ == '__main__':
	fourtwentyblazeitup()
