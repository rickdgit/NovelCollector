#!/usr/bin/python
#-*- coding: utf-8 -*-
class charpters(object):
    def __init__(self,websiteProfile,link):
    #  def __init__(self,websiteProfile,link,CurrentCharLink,htmlContent,Nname,charNum,charName,indexLink,text,nextCharlink,PrevLink):
        self.websiteProfile = websiteProfile
        self.link = link
        self.htmlContent =CurrentCharLink=''
        self.Nname = self.charNum =self.charName = self.indexLink = self.nextCharlink = self.PrevLink = ''
        self.text= ''
    def toFile(self,path,fileName):
        pass
    def toString(self):
        c = u"\u3002"
        d = ''.join([c,'\n'])
        e = u"\u201d"
        f = ''.join([e,'\n'])
        return ''.join([self.charNum,'--',self.charName,'\n',self.text]).replace(e,f).replace(c,d).encode('utf-8')
