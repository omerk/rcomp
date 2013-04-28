#!/usr/bin/env python

import sys, requests

#URL = "http://httpbin.org/post"
URL = "http://localhost:5000/compile"

if ( len(sys.argv) < 2 ):
	print "Not enough args"
	sys.exit(1);
else:
	files = {}

	for f in sys.argv[1:]:
		files[f] = open(f, 'rb')

	r = requests.post(URL, files=files)

	print r.text

