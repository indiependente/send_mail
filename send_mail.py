#! /usr/bin/python

import os
import sys
import json
import urllib2
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(email):
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
	s = smtplib.SMTP(email['smtp'] + ":" + email['port'])
	s.ehlo()
	s.starttls()
	s.login(email['username'], email['password'])
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(sndr, rcvr, msg.as_string())
	s.quit()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise ValueError('Usage: python send_mail.py <email.json>')

	FILENAME = sys.argv[1]

	with open(FILENAME) as f:
		email = json.load(f)
		send(email)