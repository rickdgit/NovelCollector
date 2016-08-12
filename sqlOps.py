import MySQLdb
class sqlOperation(object):
    def __init__(self,dbHost,dbPort,dbName,dbUid,dbPd):
        self.dbCon = self.cursor = ""
        try:
            if(dbPort != 12580):
        	self.dbCon = MySQLdb.connect(host=dbHost,user=dbUid,passwd=dbPd,db=dbName)
                print(dbPort)
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
        query = "insert into "+tbName+" ("+value+") values ("+keys+");"
        print(query+"\n")
        return query
        #  self.cursor.execute(query)

    def updateElement(self,tbName,dic,condition):
        atrbs = ""
        for k,v in dic.iteritems():
            atrbs += k+"="+v+","
        atrbs = atrbs[:-1]
        query = "update "+tbName+" set "+atrbs
        if(condition != ""):
            query += " where "+condition
        print(query+"\n")
        return query

    def deleteElement(self,tbName,condition):
        atrbs = ""
        for k in condition.iteritems():
            atrbs += k+","
        atrbs = atrbs[:-1]
        query = "delete from"+tbName+" where "+atrbs
        print(query+"\n")
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
        return query
    #OPs

#Book
    def addBook(self,bkName,author,indexLink,totalCharNum):
        dic = {'bkName':bkName,'author':author,'indexLink':indexLink,'totalCharNum':totalCharNum}
        return insertElement('books',dic)

    def getBookInfoByID(self,bookID):
        condition = "bookID = "+bookID
        atrbName = "*"
        tbName = "books"
        return retrieveElement(atrbName,tbName,condition)

    def deleteBook(self,whereA,cmpOp,whereB):
        tbName = "books"
        return deleteElement(tbName,combineWhere(whereA,cmpOp,whereB))
#
#<<<<<<< Updated upstream
    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        return insertElement('CharactersTable',dic)
#=======
    def getBookInfoByName(self,bookName):
        condition = "bookName = "+bookName
        atrbName = "*"
        tbName = "books"
        retrieveElement(atrbName,tbName,condition)
#>>>>>>> Stashed changes

    def getBookInfosByAuthor(self,author):
        condition = "author = "+author
        atrbName = "*"
        tbName = "books"
        return retrieveElement(atrbName,tbName,condition)

    def updateBook(self,attr,values,whereA,cmpOp,whereB):
        tbName = "books"
        dic = {}
        for i in range(len(attr)):
            dic[attr[i]] = values[i]
        return updateElement(tbName,dic,combineWhere(whereA,cmpOp,whereB))


#Char related

    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        return insertElement('CharactersTable',dic)

    def getChars(self,atrbName,bookID,staratChar,endChar):
        condition = "bookID = "+bookID
        if endChar != -1 :
            condition += "CharNum <= "+str(endChar)
            if startChar != -1 :
                condition += " AND "
        if startChar != -1 :
            condition +=  "CharNum > "+str(startatChar)
        return retrieveElement(atrbName,'CharactersTable',condition)

    def deleteChars(self,whereA,cmpOp,whereB):
        tbName = "CharactersTable"
        return deleteElement(tbName,combineWhere(whereA,cmpOp,whereB))

    # def getTaskByTitle(self,title):
    #     condition = "title = "+title
    #     atrbName = "*"
    #     tbName = "tasks"
    #     retrieveElement(atrbName,tbName,condition)

#User related
    def addUser(self,uid,passwd,email):
        dic = {'uid':uid,'passwd':passwd,'email':email}
        return insertElement('user',dic)

    def updateUserPassWd(self,value,whereA,cmpOp,whereB):
        tbName = "user"
        dic = {'passWd':value}
        return updateElement(tbName,dic,combineWhere(whereA,cmpOp,whereB))

    def updateUserEmail(self,value,whereA,cmpOp,whereB):
        tbName = "user"
        dic = {'email':value}
        return updateElement(tbName,dic,combineWhere(whereA,cmpOp,whereB))

#WebPerf related
    def addWebsetPerf(self,websiteAddr,charOrder,POST,encoding,removeTags,textXPathKey,titleXPathKey,indexXPathKey,nextCharXPathKey,searchXpath):
        dic = {'websiteAddr':websiteAddr,'charOrder':charOrder,'POST':POST,'encoding':encoding,'removeTags':removeTags,'textXPathKey':textXPathKey,'titleXPathKey':titleXPathKey,'indexXPathKey':indexXPathKey,'nextCharXPathKey':nextCharXPathKey,'searchXpath':searchXpath}
        return insertElement('websitePerf',dic)

    def getAWebsitePerfByWebsiteAddr(self,websiteAddr):
        #return a single websitePerf obj
        condition = "websiteAddr = "+websiteAddr
        atrbName = "*"
        tbName = "websitePerf"
        return retrieveElement(atrbName,tbName,condition)

    def getAllWebsitePerf(self):
        #return a dic of websiteperfs objects
        condition = ""
        atrbName = "*"
        tbName = "websitePerf"
        return retrieveElement(atrbName,tbName,condition)

    def strToWebsitePerf(self,string):
        #conver receiving string from db to a websiteperfs objects
        pass

#Task related
    def addTask(self):
        #select the task periority
        dic = {'bookID':bookID,'uid':uid,'bkName':bkName,'IndexLink':IndexLink,'currentChar':currentChar,'startChar':startChar,'endChar':endChar}
        return insertElement('user',dic)

    def getTaskByTaskID(self,number):
        condition = "number = "+number
        atrbName = "*"
        tbName = "tasks"
        return retrieveElement(atrbName,tbName,condition)

    def getAUserAllTask(self,uid):
        condition = "uid = "+uid
        atrbName = "*"
        tbName = "tasks"
        return retrieveElement(atrbName,tbName,condition)

    def getAUserTaskByBookID(self,uid,bookID):
        condition = "uid = "+uid + "and bookID = "+bookID
        atrbName = "*"
        tbName = "tasks"
        return retrieveElement(atrbName,tbName,condition)

    def updateOneUserReadingChar(self,bookID,uid,endChar):
        #Update read chars for only one user
        tbName = "tasks"
        dic = {'endChar':endChar}
        return updateElement(tbName,dic,combineWhere(["uid","bookID"],["=","="],[uid,bookID]))

    def updateAllUsersReadingChar(self,bookID,endChar):
        #Used for update all user for a book's reading stage for one book
        tbName = "tasks"
        dic = {'endChar':endChar}
        return updateElement(tbName,dic,combineWhere(["bookID"],["="],[bookID]))

    def updateTaskStartCharForUserWithBookID(self,uid,bookID,startChar):
        tbName = "tasks"
        dic = {'startChar':startChar}
        return updateElement(tbName,dic,combineWhere(["uid","bookID"],["=","="],[uid,bookID]))

    def updateTaskStartCharForUserWithBookName(self,uid,bookName,startChar):
        tbName = "tasks"
        dic = {'startChar':startChar}
        return updateElement(tbName,dic,combineWhere(["uid","bookName"],["=","="],[uid,bookName]))

    def updateTaskEndCharForUserWithBookID(self,uid,bookID,endChar):
        tbName = "tasks"
        dic = {'endChar':endChar}
        return updateElement(tbName,dic,combineWhere(["uid","bookID"],["=","="],[uid,bookID]))

    def updateTaskEndCharForUserWithBookName(self,uid,bookName,endChar):
        tbName = "tasks"
        dic = {'endChar':endChar}
        return updateElement(tbName,dic,combineWhere(["uid","bookName"],["=","="],[uid,bookName]))

    def updateTaskSendingFeqForUserWithBookID(self,uid,bookID,SendingFeq):
        tbName = "tasks"
        dic = {'SendingFeq':SendingFeq}
        return updateElement(tbName,dic,combineWhere(["uid","bookID"],["=","="],[uid,bookID]))

    def updateTaskSendingFeqForUserWithBookName(self,uid,bookName,SendingFeq):
        tbName = "tasks"
        dic = {'SendingFeq':SendingFeq}
        return updateElement(tbName,dic,combineWhere(["uid","bookName"],["=","="],[uid,bookName]))

    #helper methods
    def combineWhere(whereA,cmpOp,whereB):
        where = ""
        if(whereA != NULL and cmpOp != NULL and whereB != NULL):
            for i in range(len(whereA)):
                where += whereA[i]+cmpOp[i]+whereB[i]
        return where
