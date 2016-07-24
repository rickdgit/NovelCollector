class websiteProfile(object):
    def __init__(self,website,textxPathKeyW,charOrder,nextCharxPathKeyW,titlexPathKeyW,IndexGBK,indexxPathKeyW,SearchxPath,POST,encoding,user_agent,remove_tags):
        self.website = website
        self.textxPathKeyW = textxPathKeyW
        self.charOrder = charOrder
        self.titlexPathKeyW = titlexPathKeyW
        self.nextCharxPathKeyW = nextCharxPathKeyW
        self.indexxPathKeyW =indexxPathKeyW
        self.IndexGBK = IndexGBK
        self.SearchxPath = SearchxPath
        self.POST = POST
        self.encoding = encoding
        self.user_agent=user_agent
        self.remove_tags =  remove_tags

    def toString(self):
        pass
