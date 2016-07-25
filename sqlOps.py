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
    def insertElement(self,tbName,attr,values):
        pass
    def updateElement(self):
        pass
    def deleteElement(self):
        pass
    def retrieveElement(self):
        pass
    #OPs
    def addBook(self):
        pass
    def addChars(self):
        pass
    def addWebsetPerf(self):
        pass
    def addTask(self):
        pass
    def getMultiChars(self,bookid,staratChar,endChar):
        pass
    def getSingleChars(self):
        pass
    def getBook(self):
        pass
    def getTask(self):
        pass
    #  def deleteBook(self):
    #      pass
    #  def deleteChars(self):
    #      pass
