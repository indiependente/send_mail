#! /usr/bin/python
"""
author: indiependente (Francesco Farina)
email: rockerg991@gmail.com
"""

import os
import sys
import argparse
import threading
import json
import urllib2
import smtplib
import copy

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(email, num, creds=None):
	CWD = os.getcwd()

	sndr = email['from']
	rcvr = email['to']

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = email['subject']
	msg['From'] = sndr
	msg['To'] = rcvr

	# Create the body of the message (a plain-text and an HTML version).
	text = email['plaintext'] # write the plain text payload here
	# assuming the HTML payload is local
	
	html = urllib2.urlopen("file://" + CWD + "/" + email['html_file']).read()
	# print html
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')


	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via an SMTP server.
	if creds is None:
		server = email['smtp']
		port = email['port']
		username = email['username']
		password = email['password']
	else:
		server = creds['smtp']
		port = creds['port']
		username = creds['username']
		password = creds['password']

	s = smtplib.SMTP(server + ":" + port)
	s.ehlo()
	s.starttls()
	s.login(username, password)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(sndr, rcvr, msg.as_string())
	s.quit()
	print '[%d] SENT' % num

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', type = str, help='The JSON input file name - must be in the current working directory')
	parser.add_argument('-b', '--batch', type = int, help='Batch mode - it will pick the first email object from the input file and send <BATCH> emails. It will append a counter to the subject of every email being sent.')
	parser.add_argument('-c', '--credentials', type = str, help='Read credentials from external file - applies those credentials to every email')
	args = parser.parse_args()
	
	if args.credentials is None:
		creds = None
	else:
		creds = json.load(open(args.credentials))

	with open(args.filename) as f:
		emails = json.load(f)
		threads = []
		if args.batch is None:
			for i, email in enumerate(emails):
				print '[%d] Sending email to %s' % (i, email['to'])
				t = threading.Thread(target = send, args = (email, i, creds))
				threads.append(t)
				t.start()
		else:
			for i in xrange(args.batch):
				template = copy.deepcopy(emails[0])
				template['subject'] = template['subject'] + ' ' + str(i+1)
				print '[%d] Sending email to %s' % (i, template['to'])
				t = threading.Thread(target = send, args = (template, i, creds))
				threads.append(t)
				t.start()