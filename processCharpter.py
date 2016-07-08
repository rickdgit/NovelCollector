# -*- coding: utf-8 -*-
import urllib2,re
from lxml import etree,html
from multiprocessing.dummy import Pool as ThreadPool 
from lxml.html.clean import clean_html,Cleaner
import sched,time
from charpters import charpters
from book import book
from websiteProfile import websiteProfile
#TODO:
#  2.Sending Email  - so that we could send Emails to Kindle
#  3.MultiThreads for eachbook or multi Charpters

#DONE
#  1.Finish load Reqs - could read requests form file
#  4.Figure out the getNextChar by page link garbash words


class Ser(object):

    def main(self):
        print("Server Started")
        #  self.loadReqs('aName')
        books = self.loadReqs('settings')
        #PROCESS BOOK

        for abook in books:
            print(abook.bkname)
            self.processBook(abook)
            self.processResult(abook)
        #  pool = ThreadPool(4)
        #  rest = pool.map(self.processBook,books)
        #  #  self.processResult(rest[0])
        #  pool.map(self.processResult,rest)
        #  pool.close()
        #  print(time.time())

    #Load Setting files  then call processBook to get Book Infos - then processResult
    def loadReqs(self,fileName):
        #Load Requests from a file.
        #Set requests to Book object
        books = []
        bk = [i for i in range(0,5)]
        try:
            f = open(fileName,"rb+")
        except:
            print("ERROR: Setting file can not open")
        # files = f.read()
        for i in re.findall(r'\$.+\n!.+\n!.+\n!.+\n\$.+',f.read(),re.M|re.I):
            a = 0
            i = ''.join([i,'\n'])
            ops = re.findall(r'.*\n',i,re.M|re.I)
            for r in ops:
                # ress = re.search(r'\[[a-zA-Z\u4e00-\u9fa5_]*\]',r) 
                ress = re.search(r'\[.*\]',r) 
                #  bk = [res.group().replace("[","").replace("]","") if res.group()!= '[]' else '' for res in [re.search(r'\[.*\]',r) for r in ops]]
                if(ress.group() != '[]'):
                    bk[a]= ress.group().replace("[","").replace("]","")
                    print("==>>  %s <->  %s"%(bk[0],ress.group()))
                    a+=1
            #  if not bk:
            books += [book(bk[0],bk[1],bk[2],int(bk[3]),int(bk[4]))]

        print(len(books))
        return books
        
        


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
        print("START: Process BOOK")
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
                print(x)
                if(profile.charOrder == 0):
                    #inorder
                    link = ''.join([profile.website,indexArr[x]])
                else:
                    link = ''.join([profile.website,indexArr[len(indexArr)-1-x]])
                cha = charpters(profile,abook.website)
                cha.CurrentCharLink = link
                print('LINK %s'%link)
                cha.htmlContent = self.processPage(link,cha.websiteProfile)
                #  print("CONTENT: %s"%cha.htmlContent)
                #  cha.charName = self.processCharTitle(cha)
                cha.text = self.processContent(cha)
                abook.chars += [cha]
            print("Book Process by Index DONE")
        print("FINISH: Process BOOK")
        return abook
        

    def processIndex(self,abook,model):
        print("START: Process Index")
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
            print("FINISH: Process INDEX")
            return res
        else:
            #from charNumStart to charNumEnd
            print("Index arr:%d"%len(s))
            print("FINISH: Process INDEX")
            return s

    def processPage(self,url,profile):
        page = None
        res = None
        print("START: Process Page")
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
        print("FINISH: Process Page")
        #  print(page)
        res = page
        del page
        return res
        
    def processContent(self,charpter):
        #get website content - text  and process out the text
        print("START: Process CONTENT")
        element = etree.HTML(charpter.htmlContent)
        #  print(charpter.htmlContent)
        s = element.xpath(charpter.websiteProfile.textxPathKeyW)
        text =''
        for t in s:
            #  print(t)
            try:
                #  text = ''.join([text,t.encode('ISO-8859-1')])
                text = ''.join([text,t])
            except:
                pass
        print("FINISH: Process CONTENT")
        #  print("Test is %s\n"%text)
        return text

    def processnextCharLink(self,charpter):
        print("START: Process NextCharLINK")
        #get html content of a char page, process it and figure out the next char link
        element = etree.HTML(charpter.htmlContent)
        x = element.xpath(charpter.websiteProfile.nextCharxPathKeyW)
        print("FINISH: Process NextCharLINK")
        return x[0]
    def processCharTitle(self,charpter):
        print("START: Process CharTitle")
        #get html content of a char page, process it and figure out the next char link
        element = etree.HTML(charpter.htmlContent)
        x = element.xpath(charpter.websiteProfile.titlexPathKeyW)
        #  print(x[0].encode('ISO-8859-1'))
        print("FINISH: Process CharTitle")
        return x[0].encode('ISO-8859-1')


    def processResult(self,abook):
        content = ''
        for x in abook.chars:
            content = ''.join([content,x.toString().encode('utf-8')])
        fileName = ''.join([abook.bkname,'.txt'])
        self.saveToFile(fileName,content)

    def sendByMail(self,fileName):
        pass

    def saveToFile(self,fileName,content):
        fw = open(fileName,"a")
        fw.write(content)
        fw.close()


def main():
    ser = Ser()
    ser.main()

if (__name__ == '__main__'):
    main()
