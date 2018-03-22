# -*- coding: UTF-8 -*-
from PageObject.Login.Page import Page
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OrderingUITest(ParametrizedTestCase):

    def testOpenOrderingUI(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/OrderingUI/OpenOrderingUI.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = Page(app)
        page.operate()
        page.checkPoint()

    def testMyExclusive(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/OrderingUI/MyExclusive.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = Page(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(OrderingUITest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OrderingUITest, cls).tearDownClass()
