#!/usr/bin/env python

import os
import subprocess
from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "incoming"

def compile(source):
	p = subprocess.Popen(['gcc', '-Wall', source], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return [ {"out": out, "err": err} ]

@app.route('/compile', methods=['POST'])
def handle_upload():
	print "number of files: " + str(len(request.files))

	response = {}

	for f in request.files:
		upload = request.files[f]
		uploadsaved = os.path.join( app.config['UPLOAD_FOLDER'], secure_filename(upload.filename) )
		upload.save(uploadsaved)
		response[upload.filename] = compile(uploadsaved)

	return str(response)


if __name__ == '__main__':
	app.debug = True
	app.run()

