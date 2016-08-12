import unittest
from sqlOps import *

a = sqlOperation('localhost',3306,'test','tester','Test1ng!!!')
a.testInit()

class test_sqlOperations(unittest.TestCase):
    def setUp(self):
        self.sqlOps = sqlOperation('localHost','testOps','operations','fireinthehole!')
        self.sqlOps.dbInit()

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
        self.assertEqual(self.sqlOps.insertElement("user",{'uid':011})
            ,"insert into user (uid) values ('011')",
            '\nError[Insert]: can not insert single value & key')

    def test_insertElement_multi(self):
        self.assertEqual(self.sqlOps.insertElement("user",{'uid':011,'bookID':012})
            ,"insert into user (uid,bookID) values ('011,012')",
            '\nError[Insert]: can not insert multiple values & keys')

    #update element test
    def test_updateElement_single_noCondi(self):
        self.assertEqual(self.sqlOps.updateElement("user",{'uid':013},'')
            ,"update user set uid = 013",
            '\nError[Insert]: can not update single value with no condition')

    def test_updateElement_single_withCondi(self):
        self.assertEqual(self.sqlOps.updateElement("user",{'uid':013},'bookID = 100')
            ,"update user set uid = 013 where bookID = 100",
            '\nError[Insert]: can not update single value with condition')

    def test_updateElement_multi_noCondi(self):
        self.assertEqual(self.sqlOps.updateElement("user",{'uid':013,'bookID':014},"")
            ,"update user set uid = '013', bookID = 014",
            '\nError[Insert]: can not update multiple value with no condition')

    def test_updateElement_multi_withCondi(self):
        self.assertEqual(self.sqlOps.updateElement("user",{'uid':013,'bookID':014},'bookID = 100')
            ,"update user set uid = '013', bookID = 014 where bookID = 100",
            '\nError[Insert]: can not update multiple value with condition')

    #delete element test
    def test_deleteElement_noCondi(self):
        self.assertEqual(self.sqlOps.deleteElement("user",'')
            ,"delete from user",
            'Error[Insert]: can not delete with no condition')

    def test_deleteElement_withCondi(self):
        self.assertEqual(self.sqlOps.deleteElement("user",'bookID = 100')
            ,"delete from user where bookID = 100",
            '\nError[Insert]: can not delete with condition')

    #select element test
    def test_retrieveElement_single_noCondi(self):
        self.assertEqual(self.sqlOps.retrieveElement("uid","user","")
            ,"select uid from user",
            '\nError[Insert]: can not select single value with no condition')

    def test_retrieveElement_single_withCondi(self):
        self.assertEqual(self.sqlOps.retrieveElement("uid","user",'bookID = 100')
            ,"select uid from user where bookID = 100",
            '\nError[Insert]: can not select single value with condition')

    def test_retrieveElement_multi_noCondi(self):
        self.assertEqual(self.sqlOps.retrieveElement("uid","user,bookID","")
            ,"select uid,bookID from user",
            '\nError[Insert]: can not select multiple value with no condition')

    def test_retrieveElement_multi_withCondi(self):
        self.assertEqual(self.sqlOps.retrieveElement("uid","user,bookID",'bookID = 100')
            ,"select uid,bookID from user where bookID = 100",
            '\nError[Insert]: can not select multiple value with condition')

    #book test
    def test_addBook(self):
        self.assertEqual(self.sqlOps.addBook("testBook","tester","www.justAtest.com",998)
            ,"insert into books (bkName,author,indexLink,totalCharNum) values ('testBook','tester','www.justAtest.com',998",
            '\nError[Insert]: can not add a book')

    def test_getBookInfoByID(self):
        self.assertEqual(self.sqlOps.retrieveElement("uid","user","")
            ,"select uid from user",
            '\nError[Insert]: can not select single value with no condition')
