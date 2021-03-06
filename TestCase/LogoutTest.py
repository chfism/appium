# -*- coding: UTF-8 -*-
from PageObject.Login.Page import Page
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LogoutTest(ParametrizedTestCase):

    def testLogout(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/Login/Logout.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = Page(app)
        page.operate()
        #driver session 为何会在退出按钮按下后清空？
        #page.checkPoint()


    @classmethod
    def setUpClass(cls):
        super(LogoutTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LogoutTest, cls).tearDownClass()
