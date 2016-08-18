import MySQLdb
class sqlOperation(object):
    def __init__(self,dbHost,dbPort,dbName,dbUid,dbPd):
        self.dbCon = self.cursor = ""
        try:
            if(dbPort == 3306):
        	self.dbCon = MySQLdb.connect(host=dbHost,user=dbUid,passwd=dbPd,db=dbName)
            else:
        	self.dbCon = MySQLdb.connect(host=dbHost,user=dbUid,passwd=dbPd,db=dbName,dbPost=dbPort)
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
            #  self.cursor.execute("test Query lol")
            pass
        except :
            self.dbInit()

    #helper methods
    def combineWhere(self,whereA,cmpOp,whereB):
        where = ""
        if(whereA != None and cmpOp != None and whereB != None and whereA != '' and cmpOp != '' and (cmpOp != 'isNull' and whereB != '')):
            for i in range(0,len(whereA)):
                where += whereA[i]+cmpOp[i]+"'"+whereB[i]+"', "
        where = where[:-2]
        return where

    #CRUD
    def insertElement(self,tbName,dic):
        value = keys = ""
        for k,v in dic.iteritems():
            value += k+","
            keys += "'"+str(v)+"',"
            print(value)
            print(keys)
        value = value[:-1]
        keys = keys[:-1]
        query = "insert into "+tbName+" ("+value+") values ("+keys+")"
        print(query+"\n")
        self.cursor.execute(query)
        return query

    def updateElement(self,tbName,dic,condition):
        atrbs = ""
        for k,v in dic.iteritems():
            atrbs += k+" = '"+v+"', "
        atrbs = atrbs[:-2]
        query = "update "+tbName+" set "+atrbs+" "
        if(condition != ""):
            query += "where "+condition
        print(query+"\n")
        self.cursor.execute(query)
        return query

    def deleteElement(self,tbName,condition): 
        query = "delete from "+tbName+" where "+condition
        print(query+"\n")
        self.cursor.execute(query)
        return query
    # def retrieveMultiElement(self,tbName,condition):
    #     query = "select * from "+tbName+"where "+ condition
    #     print(query)
    #     #  self.cursor.execute(query)
    def retrieveElement(self,atrbName,tbName,condition):
        query = "select "+atrbName+" from "+tbName
        if condition != "" :
            query += " where "+condition
        print(query+"\n")
        self.cursor.execute(query)
        return query
    #OPs

#Book
    def addBook(self,bkName,author,indexLink,totalCharNum):
        dic = {'bkName':bkName,'author':author,'indexLink':indexLink,'totalCharNum':totalCharNum}
        return self.insertElement('books',dic)

    def getBookInfoByID(self,bookID):
        condition = "bookID = '"+bookID+"'"
        atrbName = "*"
        tbName = "books"
        return self.retrieveElement(atrbName,tbName,condition)

    def deleteBook(self,whereA,cmpOp,whereB):
        tbName = "books"
        return self.deleteElement(tbName,self.combineWhere(whereA,cmpOp,whereB))

    def getBookInfoByName(self,bookName):
        condition = "bkName = '"+bookName+"'"
        atrbName = "*"
        tbName = "books"
        return self.retrieveElement(atrbName,tbName,condition)

    def getBookInfosByAuthor(self,author):
        condition = "author = '"+author+"'"
        atrbName = "*"
        tbName = "books"
        return self.retrieveElement(atrbName,tbName,condition)

    def updateBook(self,attr,values,whereA,cmpOp,whereB):
        tbName = "books"
        dic = {}
        for i in range(len(attr)):
            dic[attr[i]] = values[i]
        return self.updateElement(tbName,dic,self.combineWhere(whereA,cmpOp,whereB))


#Char related

    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        return self.insertElement('CharactersTable',dic)

    def getChars(self,atrbName,bookID,startChar,endChar):
        condition = "bookID = '"+bookID+"'"
        if endChar != "-1" :
            condition += " and CharNum <= '"+str(endChar)+"'"
            if startChar != "-1" :
                condition += " and "
        if startChar != "-1" :
            condition +=  "CharNum > '"+str(startChar)+"'"
        return self.retrieveElement(atrbName,'CharactersTable',condition)

    def deleteChars(self,whereA,cmpOp,whereB):
        tbName = "CharactersTable"
        return self.deleteElement(tbName,self.combineWhere(whereA,cmpOp,whereB))

    # def getTaskByTitle(self,title):
    #     condition = "title = "+title
    #     atrbName = "*"
    #     tbName = "tasks"
    #     retrieveElement(atrbName,tbName,condition)

#User related
    def addUser(self,uid,passwd,email):
        dic = {'passwd':passwd,'email':email}
        return self.insertElement('user',dic)

    def updateUserPassWd(self,value,whereA,cmpOp,whereB):
        tbName = "user"
        dic = {'passwd':value}
        return self.updateElement(tbName,dic,self.combineWhere(whereA,cmpOp,whereB))

    def updateUserEmail(self,value,whereA,cmpOp,whereB):
        tbName = "user"
        dic = {'email':value}
        return self.updateElement(tbName,dic,self.combineWhere(whereA,cmpOp,whereB))

#WebPerf related
    def addWebsetPerf(self,websiteAddr,charOrder,POST,encoding,removeTags,textXPathKey,titleXPathKey,indexXPathKey,nextCharXPathKey,searchXpath):
        dic = {'websiteAddr':websiteAddr,'charOrder':charOrder,'POST':POST,'encoding':encoding,'removeTags':removeTags,'textXPathKey':textXPathKey,'titleXPathKey':titleXPathKey,'indexXPathKey':indexXPathKey,'nextCharXPathKey':nextCharXPathKey,'searchXpath':searchXpath}
        return self.insertElement('websitePerf',dic)

    def getAWebsitePerfByWebsiteAddr(self,websiteAddr):
        #return a single websitePerf obj
        condition = "websiteAddr = '"+websiteAddr+"'"
        atrbName = "*"
        tbName = "websitePerf"
        return self.retrieveElement(atrbName,tbName,condition)

    def getAllWebsitePerf(self):
        #return a dic of websiteperfs objects
        condition = ""
        atrbName = "*"
        tbName = "websitePerf"
        return self.retrieveElement(atrbName,tbName,condition)

    def strToWebsitePerf(self,string):
        #conver receiving string from db to a websiteperfs objects
        pass

#Task related
    def addTask(self,bookID,uid,bkName,IndexLink,currentChar,startChar,endChar):
        #select the task periority
        dic = {'bookID':bookID,'uid':uid,'bkName':bkName,'IndexLink':IndexLink,'currentChar':currentChar,'startChar':startChar,'endChar':endChar}
        return self.insertElement('tasks',dic)

    def getTaskByTaskID(self,number):
        condition = "number = "+number
        atrbName = "*"
        tbName = "tasks"
        return self.retrieveElement(atrbName,tbName,condition)

    def getAUserAllTask(self,uid):
        condition = "uid = "+uid
        atrbName = "*"
        tbName = "tasks"
        return self.retrieveElement(atrbName,tbName,condition)

    def getAUserTaskByBookID(self,uid,bookID):
        condition = "uid = "+uid + " and bookID = "+bookID
        atrbName = "*"
        tbName = "tasks"
        return self.retrieveElement(atrbName,tbName,condition)

    def updateAllUsersReadingChar(self,bookID,endChar):
        #Used for update all user for a book's reading stage for one book
        tbName = "tasks"
        dic = {'endChar':endChar}
        return self.updateElement(tbName,dic,self.combineWhere(["bookID"],["="],[bookID]))

    def updateTaskStartCharForUserWithBookID(self,uid,bookID,startChar):
        tbName = "tasks"
        dic = {'startChar':startChar}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bookID"],[" = "," = "],[uid,bookID]))

    def updateTaskStartCharForUserWithBookName(self,uid,bookName,startChar):
        tbName = "tasks"
        dic = {'startChar':startChar}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bkName"],[" = "," = "],[uid,bookName]))

    def updateTaskEndCharForUserWithBookID(self,uid,bookID,endChar):
        tbName = "tasks"
        dic = {'endChar':endChar}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bookID"],[" = "," = "],[uid,bookID]))

    def updateTaskEndCharForUserWithBookName(self,uid,bookName,endChar):
        tbName = "tasks"
        dic = {'endChar':endChar}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bkName"],[" = "," = "],[uid,bookName]))

    def updateTaskSendingFeqForUserWithBookID(self,uid,bookID,SendingFeq):
        tbName = "tasks"
        dic = {'SendingFeq':SendingFeq}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bookID"],[" = "," = "],[uid,bookID]))

    def updateTaskSendingFeqForUserWithBookName(self,uid,bookName,SendingFeq):
        tbName = "tasks"
        dic = {'SendingFeq':SendingFeq}
        return self.updateElement(tbName,dic,self.combineWhere(["uid","bkName"],[" = "," = "],[uid,bookName]))

