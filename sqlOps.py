import MySQLdb
class sqlOperation(object):
    def __init__(self,dbHost,dbName,dbUid,dbPd):
        self.dbCon = self.cursor = ""
        try:
            self.dbCon = MySQLdb.connect(host=dbHost,user=dbUid,passwd=dbPd,db=dbName)
            self.cursor = self.dbCon.cursor()
            self.cursor.execute("SELECT VERSION()")
            print(self.cursor.fetchone())
        except MySQLdb.Error,e:
            print("Error with DB connection:%s"%e)

        try:
            self.testInit()
        except MySQLdb.Error,e:
            print("Error with DB initinalization:%s"%e)
    def dbInit(self):
        print(self.cursor)

    def testInit(self):
        try:
            #Check all table exists
            #Or check first element in table
            self.cursor.execute("test Query lol")
        except :
            self.dbInit()
    #CRUD
    def insertElement(self,tbName,dic):
        value = keys = ""
        for k,v in dic.iteritems():
            value += k+","
            keys += v+","
        value = value[:-1]
        keys = keys[:-1]
        query = "insert into "+tbName+"("+value+") values ("+keys+");"
        print(query)
        #  self.cursor.execute(query)

    def updateElement(self,tbName,dic):
        atrbs = ""
        for k,v in dic.iteritems():
            atrbs += k+"="+v+","
        atrbs = atrbs[:-1]
        query = "update "+tbName+" set "+atrbs
        print(query)


    def deleteElement(self):
        pass
    # def retrieveMultiElement(self,tbName,condition):
    #     query = "select * from "+tbName+"where "+ condition
    #     print(query)
    #     #  self.cursor.execute(query)
    def retrieveElement(self,atrbName,tbName,condition):
        query = "select "+atrbName+" from "+tbName
        if condition != "" :
            query += " where "+condition
        print(query)
    #OPs

#Book
    def addBook(self,bkName,author,indexLink,totalCharNum):
        dic = {'bkName':bkName,'author':author,'indexLink':indexLink,'totalCharNum':totalCharNum}
        insertElement('books',dic)

    def getBookInfoByID(self,bookID):
        condition = "bookID = "+bookID
        atrbName = "*"
        tbName = "books"
        retrieveElement(atrbName,tbName,condition)
    def deleteBook(self):
        pass

    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        insertElement('CharactersTable',dic)

    def getBookInfosByAuthor(self,author):
        condition = "author = "+author
        atrbName = "*"
        tbName = "books"
        retrieveElement(atrbName,tbName,condition)

    def updateBook(self,attr,values):
        tbName = "books"
        dic = {}
        for i in range(len(attr))
            dic[attr[i]] = values[i]
        updateElement(tbName,dic)


#Char related

    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        insertElement('CharactersTable',dic)

    def getChars(self,atrbName,bookID,staratChar,endChar):
        condition = "bookID = "+bookID
        if endChar != -1 :
            condition += "CharNum <= "+str(endChar)
            if startChar != -1 :
                condition += " AND "
        if startChar != -1 :
            condition +=  "CharNum > "+str(startatChar)
        retrieveElement(atrbName,'CharactersTable',condition)

    def deleteChars(self):
        pass

    # def getTaskByTitle(self,title):
    #     condition = "title = "+title
    #     atrbName = "*"
    #     tbName = "tasks"
    #     retrieveElement(atrbName,tbName,condition)

#User related
    def addUser(self):
        pass
    def updateUserPassWd(self):
        pass
    def updateUserEmail(self):
        pass

#WebPerf related
    def addWebsetPerf(self,websiteAddr,charOrder,POST,encoding,removeTags,textXPathKey,titleXPathKey,indexXPathKey,nextCharXPathKey,searchXpath):
        dic = {'websiteAddr':websiteAddr,'charOrder':charOrder,'POST':POST,'encoding':encoding,'removeTags':removeTags,'textXPathKey':textXPathKey,'titleXPathKey':titleXPathKey,'indexXPathKey':indexXPathKey,'nextCharXPathKey':nextCharXPathKey,'searchXpath':searchXpath}
        insertElement('websitePerf',dic)
    def getAWebsitePerfByWebsiteAddr(self,WebsiteAddr):
        #return a single websitePerf obj
        pass
    def getAllWebsitePerf(self):
        #return a dic of websiteperfs objects
        pass
    def strToWebsitePerf(self,string):
        #conver receiving string from db to a websiteperfs objects
        pass

#Task related
    def addTask(self):
        #select the task periority
        dic = {'bookID':bookID,'uid':uid,'bkName':bkName,'IndexLink':IndexLink,'currentChar':currentChar,'startChar':startChar,'endChar':endChar}
        insertElement('user',dic)

    def getTaskByTaskID(self,number):
        condition = "number = "+number
        atrbName = "*"
        tbName = "tasks"
        retrieveElement(atrbName,tbName,condition)

    def getAUserAllTask(self):
        pass
    def getAUserTaskByBookID(self):
        pass
    def updateOneUserReadingChar(self,bookID,uid,endChar):
        #Update read chars for only one user
        dic = {}
        updateElement('readingProc',dic)

    def updateAllUsersReadingChar(self,bookID,endChar):
        #Used for update all user for a book's reading stage for one book
        pass

    def updateTaskStartCharForUserWithBookID(self,uid,bookID):
        pass
    def updateTaskStartCharForUserWithBookName(self,uid,bookName):
        pass
    def updateTaskEndCharForUserWithBookID(self,uid,bookID):
        pass
    def updateTaskEndCharForUserWithBookName(self,uid,bookName):
        pass
    def updateTaskSendingFeqForUserWithBookID(self,uid,bookID):
        pass
    def updateTaskSendingFeqForUserWithBookName(self,uid,bookName):
        pass
