#Novel MetaSearchEngine
Novel MetaSearchEngine is a service that grep novels from websites' search Engine, store them in MySQL database  and present the novel with its sources to user. Beside, it comes with send by email service wich can be used for SendToKindle service provided by Amazon.

Cooperate with crontab cmd in *inx system could check the update of novels periodically

It wtitten by Python 2.7 and using lxml,urllib2,MySQL-Python,smtplib

#TODOs
Update MySQL query - sqlOps.py

Refactor main processChapters.py - update main program

Update search funtion that send request to website's search engine and process the result.

Build interfaces to list contents to user.

Build web interfaces to user.

#Setup
Install relys by pip:

	pip install pinyin
	pip install MySQL-Python

##Usage:
Note: The following settings could be added manually by using MySQL client. However, for each time program runs, it will check the following files in order to update the database. 

Store the novel relate settings in setting file by follow the format:
	
	$BookName:[BookName]
	!Website:[Front page Link]
	!IndexLink:[Index Page Link]
	!StartCharNum:[Char number that you want to start grep]
	$EndingCharNum:[Char number that you want to end grep]
	=================
	
For email settings, please store the related settings inside of mail file by following format:

	$Sender:[Sender email]
	!Receiver:[Receiver Email]
	!Subject:[Subject of the email]
	!Website:[SMTP server address of the mail service provider]
	$PassWD:[Passwd that decode to base64]
	=================
	
##Setup on *inx like platform:
we shall using crontab command to run the program periodically by

	crontab -e 

Add a new service by following format

	[min] [hr] [day of month] [month] [day of week] [execute method] [executable file name] [options]

Here is an example:

	0 20,8 * * * /usr/bin/python /path/novel/processCharpter.py >>/path/novel/Novel`date +\%Y\%m\%d_\%H:\%M`.log  2>&1
