import unittest
from sqlOps import *

class test_sqlOperations(unittest.TestCase):
    def setUp(self):
        print("setUp started")
        self.sqlOps = sqlOperation('localhost',3306,'test','tester','Test1ng!!!')
        print("Connection estabilished\n")
        #  self.sqlOps.dbInit()

    def teardown(self):
        pass

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass


    #insert element test
    def test_insertElement_single(self):
        query = "insert into user (uid) values ('011')"
        testQuery = self.sqlOps.insertElement("user",{'uid':'011'})
        errorMsg = '\nError: Wrong query generated when insert single value & key.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_insertElement_multi(self):
        query = "insert into user (uid,bookID) values ('011','012')"
        testQuery = self.sqlOps.insertElement("user",{'uid':'011','bookID':'012'})
        errorMsg = '\nError: Wrong query generated when insert multiple values & keys.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #update element test
    def test_updateElement_single_noCondi(self):
        query = "update user set uid = '013'"
        testQuery = self.sqlOps.updateElement("user",{'uid':'013'},'')
        errorMsg = '\nError: Wrong query generated when update single value with no condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateElement_single_withCondi(self):
        query = "update user set uid = '013' where bookID = '100'"
        testQuery = self.sqlOps.updateElement("user",{'uid':'013'},"bookID = '100'")
        errorMsg = '\nError: Wrong query generated when update single value with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateElement_multi_noCondi(self):
        query = "update user set uid = '013', bookID = '014'"
        testQuery = self.sqlOps.updateElement("user",{'uid':'013','bookID':'014'},"")
        errorMsg = '\nError: Wrong query generated when update multiple value with no condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateElement_multi_withCondi(self):
        query = "update user set uid = '013', bookID = '014' where bookID = '100'"
        testQuery = self.sqlOps.updateElement("user",{'uid':'013','bookID':'014'},"bookID = '100'")
        errorMsg = '\nError: Wrong query generated when update multiple value with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #delete element test
    def test_deleteElement_noCondi(self):
        query = "delete from user"
        testQuery = self.sqlOps.deleteElement("user",'')
        errorMsg = '\nError: Wrong query generated when delete with no condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_deleteElement_withCondi(self):
        query = "delete from user where bookID = '100'"
        testQuery = self.sqlOps.deleteElement("user","bookID = '100'")
        errorMsg = '\nError: Wrong query generated when delete with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #select element test
    def test_retrieveElement_single_noCondi(self):
        query = "select uid from user"
        testQuery = self.sqlOps.retrieveElement("uid","user","")
        errorMsg = '\nError: Wrong query generated when select single value with no condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_retrieveElement_single_withCondi(self):
        query = "select uid from user where bookID = '100'"
        testQuery = self.sqlOps.retrieveElement("uid","user","bookID = '100'")
        errorMsg = '\nError: Wrong query generated when select single value with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_retrieveElement_multi_noCondi(self):
        query = "select uid,bookID from user"
        testQuery = self.sqlOps.retrieveElement("uid","user,bookID","")
        errorMsg = '\nError: Wrong query generated when select multiple value with no condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_retrieveElement_multi_withCondi(self):
        query = "select uid,bookID from user where bookID = '100'"
        testQuery = self.sqlOps.retrieveElement("uid","user,bookID","bookID = '100'")
        errorMsg = '\nError: Wrong query generated when select multiple value with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #book test
    def test_addBook(self):
        query = "insert into books (bkName,author,indexLink,totalCharNum) values ('testBook','tester','www.justAtest.com',998"
        testQuery = self.sqlOps.addBook("testBook","tester","www.justAtest.com",998)
        errorMsg = '\nError: Wrong query generated when add a book.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getBookInfoByID(self):
        query = "select * from books where bookID = '001'"
        testQuery = self.sqlOps.getBookInfoByID('001')
        errorMsg = '\nError: Wrong query generated when select book by ID.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_deleteBook(self):
        query = "delete from user where bookID < '150'"
        testQuery = self.sqlOps.deleteBook('bookID','<','150')
        errorMsg = '\nError: Wrong query generated when delete book.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getBookInfoByName(self):
        query = "select * from books where bkName = 'test'"
        testQuery = self.sqlOps.getBookInfoByName('test')
        errorMsg = '\nError: Wrong query generated when select book by Name.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getBookInfoByAuthor(self):
        query = "select * from books where author = 'tester'"
        testQuery = self.sqlOps.getBookInfoByAuthor('tester')
        errorMsg = '\nError: Wrong query generated when select book by Author.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateBook_single(self):
        query = "update books set bookID = '013' where totalCharNum > '100'"
        testQuery = self.sqlOps.updateBook({'bookID'},{'013'},'totalCharNum','>','100')
        errorMsg = '\nError: Wrong query generated when update a single attr of a Book.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateBook_multi(self):
        query = "update books set bookID = '013',author = 'tester' where totalCharNum > '100'"
        testQuery = self.sqlOps.updateBook({'bookID','author'},{'013','tester'},'totalCharNum','>','100')
        errorMsg = '\nError: Wrong query generated when update multiple attr of a Book.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #test Char related
    def test_addChars(self):
        query = "insert into CharactersTable (bookID,CharNum,CharTitle,CharContect) values ('001','065','test chapter','1998')"
        testQuery = self.sqlOps.addChars('001','065','test chapter','1998')
        errorMsg = '\nError: Wrong query generated when add a chapter.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getChars(self):
        query = "select * from CharactersTable where bookID = '100' and CharNum <= 50"
        testQuery = self.sqlOps.retrieveElement("*","100","-1","50")
        errorMsg = '\nError: Wrong query generated when select single value with condition.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_deleteChars(self):
        query = "delete from CharactersTable where bookID = '100'"
        testQuery = self.sqlOps.deleteChars('bookID','=','100')
        errorMsg = '\nError: Wrong query generated when delete a Character.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    #test User related
    def test_addUser(self):
        query = "insert into user (uid,passwd,email) values ('011','010101','test@test.com')"
        testQuery = self.sqlOps.addUser('011','010101','test@test.com')
        errorMsg = '\nError: Wrong query generated when add a user.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateUserPassWd(self):
        query = "update user set passwd = '010101' where uid = '011'"
        testQuery = self.sqlOps.updateUserPassWd('010101','uid','=','100')
        errorMsg = '\nError: Wrong query generated when update user passwd.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateUserEmail(self):
        query = "update user set email = 'test@test.com' where uid = '011'"
        testQuery = self.sqlOps.updateUserEmail('test@test.com','uid','=','100')
        errorMsg = '\nError: Wrong query generated when update user email.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

#test WebPerf related
    def test_addWebsetPerf(self):
        query = "insert into websitePerf (websiteAddr,charOrder,POST,encoding,removeTags,textXPathKey,titleXPathKey,indexXPathKey,nextCharXPathKey,searchXpath) values ('test.com','100','test1','test2','teat3','test4','test5','test6','test7','test8')"
        testQuery = self.sqlOps.addWebsetPerf('test.com','100','test1','test2','teat3','test4','test5','test6','test7','test8')
        errorMsg = '\nError: Wrong query generated when add a web set perf.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getAWebsitePerfByWebsiteAddr(self):
        query = "select * from websitePerf where websiteAddr = 'test.com'"
        testQuery = self.sqlOps.getAWebsitePerfByWebsiteAddr('test.com')
        errorMsg = '\nError: Wrong query generated when select websitePerf by websiteAddr.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getAllWebsitePerf(self):
        query = "select * from websitePerf"
        testQuery = self.sqlOps.getAllWebsitePerf()
        errorMsg = '\nError: Wrong query generated when select all websitePerf.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

#TEST Task related
    def test_addTask(self):
        query = "insert into tasks (bookID,uid,bkName,IndexLink) values ('100','001','test','book.com')"
        testQuery = self.sqlOps.addTask()
        errorMsg = '\nError: Wrong query generated when add a Task.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getTaskBybookID(self):
        query = "select * from tasks where bookID = '001'"
        testQuery = self.sqlOps.getTaskBybookID('001')
        errorMsg = '\nError: Wrong query generated when select task by bookID.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getAUserAllTask(self):
        query = "select * from tasks where uid = '100'"
        testQuery = self.sqlOps.getAUserAllTask('100')
        errorMsg = '\nError: Wrong query generated when select task from a user.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_getAUserTaskByBookID(self):
        query = "select * from tasks where uid = '100' bookID = '001'"
        testQuery = self.sqlOps.getAUserTaskByBookID('100','001')
        errorMsg = '\nError: Wrong query generated when select task from a user by bookID.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateAllUserReadingChar(self):
        query = "update tasks set endChar = '50' where bookID = '001'"
        testQuery = self.sqlOps.updateAllUserReadingChar('001','50')
        errorMsg = '\nError: Wrong query generated when update all user reading char.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskStartCharForUserWithBookID(self):
        query = "update tasks set startChar = '1' where uid = '011', bookID = '001'"
        testQuery = self.sqlOps.updateTaskStartCharForUserWithBookID('011','001','1')
        errorMsg = '\nError: Wrong query generated when update a user start char by book id.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskStartCharForUserWithBookName(self):
        query = "update tasks set startChar = '1' where uid = '011', bkName = 'test'"
        testQuery = self.sqlOps.updateTaskStartCharForUserWithBookName('011','test','1')
        errorMsg = '\nError: Wrong query generated when update a user start char by book name.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskEndCharForUserWithBookID(self):
        query = "update tasks set endChar = '50' where uid = '011', bookID = '001'"
        testQuery = self.sqlOps.updateTaskEndCharForUserWithBookID('011','001','50')
        errorMsg = '\nError: Wrong query generated when update a user end char by book id.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskEndCharForUserWithBookName(self):
        query = "update tasks set endChar = '50' where uid = '011', bkName = 'test'"
        testQuery = self.sqlOps.updateTaskEndCharForUserWithBookName('011','test','50')
        errorMsg = '\nError: Wrong query generated when update a user end char by book name.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskSendingFeqForUserWithBookID(self):
        query = "update tasks set SendingFeq = '10' where uid = '011', bookID = '001'"
        testQuery = self.sqlOps.updateTaskSendingFeqForUserWithBookID('011','001','50')
        errorMsg = '\nError: Wrong query generated when update a user Sending Feq by book id.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)

    def test_updateTaskSendingFeqForUserWithBookName(self):
        query = "update tasks set SendingFeq = '10' where uid = '011', bkName = 'test'"
        testQuery = self.sqlOps.updateTaskSendingFeqForUserWithBookName('011','test','50')
        errorMsg = '\nError: Wrong query generated when update a user Sending Feq by book name.\n   Test query: '+testQuery+'\nCorrect query: '+query+'\n'
        self.assertEqual((testQuery,query),errorMsg)



if __name__=='__main__':
    unittest.main()
