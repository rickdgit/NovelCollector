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
        pass
    def deleteElement(self):
        pass
    def retrieveMultiElement(self,tbName,condition):
        query = "select * from "+tbName+"where "+ condition
        print(query)
        #  self.cursor.execute(query)
    def retrieveElement(self):
        pass
    #OPs
    def addBook(self,bkName,author,indexLink,totalCharNum):
        dic = {'bkName':bkName,'author':author,'indexLink':indexLink,'totalCharNum':totalCharNum}
        insertElement('books',dic)


    def addChars(self,bookID,CharTitle,CharNum,CharContect):
        dic = {'bookID':bookID,'CharNum':CharNum,'CharTitle':CharTitle,'CharContect':CharContect}
        insertElement('CharactersTable',dic)


    def addWebsetPerf(self,websiteAddr,charOrder,POST,encoding,removeTags,textXPathKey,titleXPathKey,indexXPathKey,nextCharXPathKey,searchXpath):
        dic = {'websiteAddr':websiteAddr,'charOrder':charOrder,'POST':POST,'encoding':encoding,'removeTags':removeTags,'textXPathKey':textXPathKey,'titleXPathKey':titleXPathKey,'indexXPathKey':indexXPathKey,'nextCharXPathKey':nextCharXPathKey,'searchXpath':searchXpath}
        insertElement('websitePerf',dic)


    def addTask(self):
        #select the task periority
        dic = {'bookID':bookID,'uid':uid,'bkName':bkName,'IndexLink':IndexLink,'currentChar':currentChar,'startChar':startChar,'endChar':endChar}
        insertElement('user',dic)


    def getMultiChars(self,bookid,staratChar,endChar):
        condition = "bookID = "+bookID+ " CharNum <= "+endChar + "AND CharNum > "+startatChar 
        retrieveElement('CharactersTable',condition)


    def getSingleChars(self):
        pass
    def getBook(self):
        pass
    def getTask(self):
        pass
    def updateBook(self,attr,values):
        pass
    def updateOneUserReadingChar(self,bookID,uid,endChar):
        #Update read chars for only one user
        dic = {}
        updateElement('readingProc',dic)
        pass
    def updateUsersReadingChar(self,bookID,endChar):
        #Used for update all user for a book's reading stage for one book
        pass
    #  def deleteBook(self):
    #      pass
    #  def deleteChars(self):
    #      pass
