from PageObject import Pages


class Page:
    """
    登陆
    """

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    '''
    操作步骤
    '''

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        self.page.checkPoint()


if __name__ == "__main__":
    pass
