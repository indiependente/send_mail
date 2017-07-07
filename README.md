# send_mail.py

## Python email client
```
usage: send_mail.py [-h] [-b BATCH] filename

positional arguments:
  filename              The JSON input file name - must be in the current
                        working directory

optional arguments:
  -h, --help            show this help message and exit
  -b BATCH, --batch BATCH
                        Batch mode - it will pick the first email object from
                        the input file and send <BATCH> emails. It will append
                        a counter to the subject of every email being sent.
```
### Supported features
* Parallel threaded email sending
* Batch mode
* Multipart content
* Read HTML from file

## Email object
Main email properties listed in the JSON object.
Every email object is tied to the SMTP server that has to send it.
SMTP account credentials: `username` and `password`.

### Example emails.json file

```json
[
	{
		"from" 		:	"me@example.com",
		"to"		:	"you@example.com",
		"subject"	:	"Hey! Email 1",
		"html_file"	:	"body1.html",
		"plaintext"	:	"I am plain text 1",
		"smtp"		:	"smtp.example.com",
		"port"		:	"587",
		"username"	:	"username",
		"password"	:	"password"
	},
	{
		"from" 		:	"me@example.com",
		"to"		:	"you@example.com",
		"subject"	:	"Hey! Email 2",
		"html_file"	:	"body2.html",
		"plaintext"	:	"I am plain text 2",
		"smtp"		:	"smtp.example.com",
		"port"		:	"587",
		"username"	:	"username",
		"password"	:	"password"
	},
	{
		"from" 		:	"me@example.com",
		"to"		:	"you@example.com",
		"subject"	:	"Hey! Email 3",
		"html_file"	:	"body3.html",
		"plaintext"	:	"I am plain text3",
		"smtp"		:	"smtp.example.com",
		"port"		:	"587",
		"username"	:	"username",
		"password"	:	"password"
	}
]
```

### ToDo
- [ ] Error checking
- [ ] Email object encryption

### Feature requests
- [x] Single input file for multiple emails:
    - Provide a JSON array of email objects
- [x] Batch mode
	- Picks the first email object of the array contained in the input file and sends N copy of that email (adds a counter to the subject)