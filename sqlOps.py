import MySQLdb
class sqlOperation(object):
    def __init__(self,dbHost,dbName,dbUid,dbPd):
        self.dbCon = self.cursor = ""
        try:
            self.dbCon = MySQLdb.connect(host=dbHost,user=dbUid,passwd=dbPd,db=dbName)
            self.cursor = self.dbCon.cursor()
            self.cursor.execute("SELECT VERSION()")
            print(self.cursor.fetchone())
        #Test DB initation
        except MySQLdb.Error,e:
            print("Error with DB connection:%s"%e)
    def dbInit(self):
        print(self.cursor)

    def testInit(self):
        try:
            self.cursor.execute("test Query lol")
        except :
            self.dbInit()
