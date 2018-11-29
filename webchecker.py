import urllib.request
import smtplib
from email.message import EmailMessage


# Python script that checks if a url site is up and sends you an email if it is up or not
# WARNING: Gmail requires that you allow less secure apps to work!
# It is best to create a separate address to accomplish this task, or setup your own SMTP server
def main():
	# put in the urls you want to use in here
	urls = ['http://httpstat.us/200', 'https://www.google.com', 'http://httpstat.us/204']
	messages = []
	for url in urls:
		code = str(urllib.request.urlopen(url).getcode())
		if (code == "200"):
			messages.append("The URL " + url + " is up and running, code: " + code)
		else:
			messages.append("The URL " + url + " is DOWN, code: " + code)
	message = '\n'.join(messages)

	msg = EmailMessage()
	msg.set_content("%s" % message)

	msg['Subject'] = 'Automated report'

	fromaddr = 'senderEmail@gmail.com'
	toaddrs = 'receiverEmail@gmail.com'

	msg['From'] = fromaddr
	msg['To'] = toaddrs

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()

	username = 'senderEmail@gmail.com'
	password = 'senderEmailPassword'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.send_message(msg)
	server.quit()

main()
