#Novel Sender
Novel sender is a service that grep novels from website and send them to Kindle via amazon's kindle email address.
It cam be used to check the update of novels periodically

It wtitten by Python 2.7 and using lxml,urllib2,,smtplib

##Usage:
Sotre the novel relate content in side of setting file and follow the format:
	
	$BookName:[BookName]
	!Website:[Front page Link]
	!IndexLink:[Index Page Link]
	!StartCharNum:[Char number that you want to start grep]
	$EndingCharNum:[Char number that you want to end grep]
	=================
	
For email settings, please store the related content inside of mail file with following format:

	$Sender:[Sender email]
	!Receiver:[Receiver Email]
	!Subject:[Subject of the email]
	!Website:[SMTP server address of the mail service provider]
	$PassWD:[Passwd that decode to base64]
	=================
	
##Setup on *inx like paltform:
TBD