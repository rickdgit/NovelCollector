class book(object):
    def __init__(self,bkname,website,indexlink,charNumStart,charNumEnd):
        self.chars = []
        self.bkname = bkname
        self.website = website
        self.indexlink = indexlink
        self.indexNum = 0;
        self.charNumEnd = charNumEnd
        self.charNumStart = charNumStart
    def toString(self):
        pass
