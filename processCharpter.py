#!/usr/bin/python2.7
# coding: utf-8
import urllib2,re,smtplib,sys,datetime,pypinyin
from pypinyin import pinyin, lazy_pinyin
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from lxml import etree,html
from lxml.html.clean import clean_html,Cleaner
from charpters import charpters
from book import book
from websiteProfile import websiteProfile
from mails import mail 

from multiprocessing.dummy import Pool as ThreadPool 
import sched,time
#TODO:
#  Settings can't updated 
#  Update  Charpters - after each read 
#  MultiThreads for eachbook or multi Charpters
#  Update Load WebsiteProfile - add format check in loadReqs & len(bk)
#  Update plain txt secrets with netrc text file 
#  Use DB instead of setting file
#  Update Reading Format

#DONE
#  Finish load Reqs - could read requests form file
#  Sending Email  - so that we could send Emails to Kindle
#  Figure out the getNextChar by page link garbash words


class Ser(object):

    def main(self):
        print("Server Started")
	print(datetime.datetime.now())
        #  self.loadReqs('aName')
        books = self.loadReqs('settings','book')
        #PROCESS BOOK
        for abook in books:
            print(abook.bkname)
            self.processBook(abook)
        self.processResult(books)

    #Load Setting files  then call processBook to get Book Infos - then processResult
    def loadReqs(self,fileName,settingType):
        #Load Requests from a file.
        #Set requests to Book object
        reqs = []
        try:
            f = open(fileName,"r+")
            #Readable
            for i in re.findall(r'\$.+\n!.+\n!.+\n!.+\n\$.+',f.read(),re.M|re.I):
                bk = []
                i = ''.join([i,'\n'])
                ops = re.findall(r'.*\n',i,re.M|re.I)
                for r in ops:
                    ress = re.search(r'\[.*\]',r) 
                    #  bk = [res.group().replace("[","").replace("]","") if res.group()!= '[]' else '' for res in [re.search(r'\[.*\]',r) for r in ops]]
                    if(ress.group() != '[]'):
                        bk += [ress.group().replace("[","").replace("]","")]
                if len(bk)>0:
                    if settingType is 'book':
                        reqs += [book(bk[0],bk[1],bk[2],int(bk[3]),int(bk[4]))]
                    elif settingType is 'email':
                        reqs += [mail(bk[0],bk[1],bk[2],bk[3],bk[4])]            
                    else:
                        print("")
            f.close()
        except:
            print("ERROR: Setting file can not open")
        return reqs

    def searchDB(self,bkName,charNumStart,charNumEnd):
        #use multi thread to search book for multiple website - choose one of them
        #return book obj - pass it to process Index that contains website name,index Link, book name
        # if charNumEnd is '' - set the last char as End
        pass


    def loadWebsiteProfile(self,websitename):
        #  first = websiteProfile('http:www.2shu.cc',"//div[@id='content']",0,"/html/body//a[@href]",13,'','','ISO-8859-1','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',['br','table','tr','td'])
        website = 'http://www.uukanshu.com'
        textxPathKeyW = "/html/body//div[@id='contentbox']/child::text()"
        nextCharxPathKeyW = '/html/body//div[@class="fanye_cen"]/child::a/attribute::href'
        indexxPathKeyW = "/html/body//ul[@id='chapterList']/child::li/a/attribute::href"
        titlexPathKeyW = "/html/body//h1[@id='timu']/child::text()"
        IndexGBK = 1
        second = websiteProfile(website,textxPathKeyW,1,nextCharxPathKeyW,titlexPathKeyW,IndexGBK,indexxPathKeyW,'','','ISO-8859-1','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',['br','table','tr','td','p'])
        return second

    def processBook(self,abook):
        print("    START: Process BOOK")
        #get a book named abook
        #return no thing
        #Key part for this program
        #searchDB
        DBres = self.searchDB('name',1,2)
        #crate Charpters
        profile = self.loadWebsiteProfile(abook.website)
        chars = charpters(profile,abook.website)
        #update abook
        abook.chars += [chars]
        #processIndex
        if(abook.charNumEnd == ''):
            print("Starting process book by Set starting charpter  <==>  %d"%abook.charNumStart)
            #means to the end of whole file
            #Recurrisive go over all pages
            index = 0
            startCharLink = self.processIndex(abook,0)
            abook.chars[0].htmlContent = self.processPage(startCharLink,profile)
            
            #Process Content
            abook.chars[0].text = self.processContent(abook.chars[0])
            print('<<<<<<<<<<<<<<<')
            abook.chars[0].nextCharlink = self.processnextCharLink(abook.chars[0])
            while(abook.chars[index].nextCharlink != None):
                #Generate a base charpters
                cha = charpters(profile,abook.website)
                #Process html 
                nextLink = ''.join([abook.website,abook.chars[index].nextCharlink])
                cha.htmlContent = self.processPage(nextLink,abook.chars[index].websiteProfile)
                #  print(abook.chars[0].htmlContent)
                #  print(cha.htmlContent)
                #Process html to get text
                cha.text = self.processContent(cha)
                #Process html to get nextCharlink
                cha.nextCharlink = self.processnextCharLink(cha)
                #char # - based on index
                cha.charNum = index
                abook.chars += [cha]
                index+=1
            print("Book process by start char DONE")

        else:
            print("Starting Process book by Indexes")
            #to target chars 
            indexArr = self.processIndex(abook,1)
            profile.IndexGBK = 0

            #Process Page Range
            if(abook.charNumStart  ==-1):
                #start Char # == -1 ---> from beginning 
                #All to the end
                start = 0
            else:
                # to a specific posn
                start = abook.charNumStart
            if(abook.charNumEnd == -1):
                # end = -1 ----> to the end
                end = len(indexArr)-1
            else:
                end = abook.charNumEnd
            print("Start %d -> setting %d ,end %d -> setting %d"%(start,abook.charNumStart,end,abook.charNumEnd))

            for x in range(start,end):
                print("Char INDEX : %d"%x)
                if(profile.charOrder == 0):
                    #inorder
                    link = ''.join([profile.website,indexArr[x]])
                else:
                    link = ''.join([profile.website,indexArr[len(indexArr)-1-x]])
                cha = charpters(profile,abook.website)
                cha.CurrentCharLink = link
                cha.htmlContent = self.processPage(link,cha.websiteProfile)
                cha.charName = self.processCharTitle(cha)
                cha.charNum = str(x)
                cha.text = self.processContent(cha)
                abook.chars += [cha]
            print("Book Process by Index DONE")
        print("    FINISH: Process BOOK")
        return abook
        

    def processIndex(self,abook,model):
        print("    START: Process Index")
        #process Indexs
        index = abook.indexlink
        profile = abook.chars[0].websiteProfile
        #process index page
        html = self.processPage(index,profile)
        #process&pick links from html
        element = etree.HTML(html)
        s = element.xpath(profile.indexxPathKeyW,smart_strings=True)
        if(model == 0):
            #all to the end
            #only need to know the target index of the first char
            # if website is reverse ordered - send back the last page
            if(abook.chars[0].websiteProfile.charOrder == 0):
                res = ''.join([profile.website,s[abook.charNumStart]])
            else:
                res = ''.join([profile.website,s[-1]])
            print("    FINISH: Process INDEX")
            return res
        else:
            #from charNumStart to charNumEnd
            print("Index arr:%d"%len(s))
            abook.indexNum = len(s)
            print("    FINISH: Process INDEX")
            return s

    def processPage(self,url,profile):
        page = None
        res = None
        print("    START: Process Page")
        #grep webpage and process to text
        #Can not be charpter as input - used for both index process and concent grep
        req = urllib2.Request(url=url,headers={'User-Agent':profile})
        page = urllib2.urlopen(req)
        info = page.info()
        charset = info.getparam('charset')
        response = page.read()
        response = response.decode(charset,'ignore')
        #  if(profile.IndexGBK == 1):
        #      response = unicode(response,'GBK').encode('UTF-8')
        cleaner = Cleaner(page_structure=False,links=False,remove_tags=profile.remove_tags)
        page = cleaner.clean_html(response)
        print("    FINISH: Process Page")
        #  print(page)
        res = page
        del page
        return res
        
    def processContent(self,charpter):
        #get website content - text  and process out the text
        print("    START: Process CONTENT")
        element = etree.HTML(charpter.htmlContent)
        #  print(charpter.htmlContent)
        s = element.xpath(charpter.websiteProfile.textxPathKeyW)
        text =''
        for t in s:
            #  print(t)
            try:
                #  text = ''.join([text,t.encode('ISO-8859-1')])
                text = ''.join([text,t,'\n'])
            except:
                pass
        print("    FINISH: Process CONTENT")
        #  print("Test is %s\n"%text)
        return text

    def processnextCharLink(self,charpter):
        print("    START: Process NextCharLINK")
        #get html content of a char page, process it and figure out the next char link
        element = etree.HTML(charpter.htmlContent)
        x = element.xpath(charpter.websiteProfile.nextCharxPathKeyW)
        print("    FINISH: Process NextCharLINK")
        return x[0]


    def processCharTitle(self,charpter):
        print("    START: Process CharTitle")
        #get html content of a char page, process it and figure out the next char link
        element = etree.HTML(charpter.htmlContent)
        x = element.xpath(charpter.websiteProfile.titlexPathKeyW)
        #  print(x[0].encode('ISO-8859-1'))
        print("    FINISH: Process CharTitle")
        return x[0]

    def processResult(self,books):
        print("    START: Process Result")
        i = 2;
        for abook in books:
            content = ''
            if((abook.charNumEnd == -1 and abook.charNumStart < abook.indexNum) or abook.charNumStart < abook.charNumEnd  ):
                for x in abook.chars:
                    content = ''.join([content,x.toString()])
                bkname = (abook.bkname).decode("utf-8")#.encode('gbk')
		py = lazy_pinyin(bkname)
		name = reduce((lambda x,y : '-'.join([x,y])),py)
                fileName = ''.join([name,str(abook.charNumStart),'-',str((abook.charNumEnd,abook.indexNum)[abook.charNumEnd == -1]),'.txt'])
		print(fileName)
                #Save To File
                self.saveToFile(fileName,content)
                #Send TO Mail
                #self.sendByMail(fileName)
                #Update DB/File
                self.updateSettings('settings',abook,i)
                i += 1
            else:
                print("ERROR:Starting Char Num equals to Ending Char Num")
        print("    FINISH: Process CharTitle")

    def sendByMail(self,fileName):
        print("    START: Sending File By EMAIL")
        amail = self.loadReqs('mail','email')[0]
        sender = amail.sender
        receiver = amail.receiver
        msg = MIMEMultipart()
        msg['From']=sender
        msg['To']=receiver
        msg['Subject']= amail.subject
        body = amail.body
        msg.attach(MIMEText(body,'plain'))
        attachment = open(fileName,"rb")

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
        msg.attach(part)

        try:
            smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
            print("1 - Pass : open SMTP Connection")
            smtpObj.starttls()
            print("2 - Pass : Open SSL Connection")
            smtpObj.login(sender,amail.passWD.decode('base64'))
            print("3 - Pass : Login")
            smtpObj.sendmail(sender,receiver,msg.as_string())
            print("4 - Pass : Sent")
            smtpObj.quit()
            print("5 - Pass : Quit Email sending Program ")
        except:
            print(sys.exc_info()[0])
            print("EMAIL SENDING ERROR")
            pass

    def saveToFile(self,fileName,content):
        print("    START: Save File")
        fw = open(fileName,"w")
        #print(content)
        fw.write(content)
        fw.close()
        print("    FINISH: Save File")

    #Update settings file - such as update char #
    def updateSettings(self,fileName,reqs,lineNum):
        print("    START: UPDATE SETTING")
	time.sleep(1)
	f = open(fileName,'r')
        #with open(fileName,'r') as file:
        #    data = file.readlines()
	data = f.readlines()
	f.close()
        if(reqs.charNumEnd == -1):
            endNum =  reqs.indexNum
        else:
            endNum = reqs.charNumEnd
        data[lineNum*6-3] = data[lineNum*6-3].replace(str(reqs.charNumStart),str(endNum))
	print(data[lineNum*6-3])
	f = open(fileName,'w')
	f.writelines(data)
	f.close()
        #with open(fileName,'w') as file:
        #   file.writelines(data)
	time.sleep(1)
        print("    FINISH: UPDATE SETTING ")

def main():
    ser = Ser()
    ser.main()

if (__name__ == '__main__'):
    main()
