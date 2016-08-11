import unittest
from sqlOps import *

class TestSqlOps(unittest.TestCase):
    def test_dbConnection(selfself):
        a = sqlOperation('localhost',3306,'test','tester','Test1ng!!!')
        a.testInit()


if __name__ == '__main__':
    test_dbOps.main()
