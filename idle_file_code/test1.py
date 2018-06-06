#coding=utf-8
import unittest
from  selenium import webdriver
class Mydemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=1
    def test1(self):
        print ("before update the a in test1 is:{}".format(self.a))
        self.a=self.a+1
        print ("after update the a in test1 is:{}".format(self.a))
    def test2(self):
        print ("the value in test2 is:{}".format(self.a))
    @classmethod
    def tearDownClass(cls):
        print ("I am tearDownClass")
if __name__ == '__main__':
    unittest.main()