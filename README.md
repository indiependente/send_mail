# send_mail.py

## Python email client
Usage: `python send_mail.py emails.json`

### Supported features
* Parallel threaded email sending
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
