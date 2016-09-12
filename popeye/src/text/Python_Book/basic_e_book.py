# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 15:47:36 2014

@author: David
"""
import os
from tkinter import *

class DoXML:
    def __init__(self, name):
        self.root = Tk()
        self.S = Scrollbar(self.root)
        self.T = Text(self.root, height=40, width=120, wrap=WORD)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.file_name = name;
#        self.fh = open(self.file_name,"r")
        os.chdir("XML")
        self.fh = open(self.file_name,'rb')
        self.chapNum = 0;

    def getChar(self):
        byte = self.fh.read(1)
        ch = byte.decode("utf-8")
        while ch == '\r' or ch == '\n':
            ch = self.fh.read(1).decode("utf-8")
        return ch
      
    def getNum(self):
        n = 0;
        ch = self.getChar()
        while ch >= '0' and ch <= '9':
            n = n * 10 + ord(ch) - ord('0')
            ch = self.getChar()
        return (n, ch)
        
    def getElement(self, ch):
        if ch != '<':
            raise RuntimeError('expected <element>')
        ch = self.getChar()
        e = "";
        while ch != ">":
            e += ch
            ch = self.getChar()
        return e
            
    def processState(self, state):
        print('State is ' + state)
        if state == 'INIT':
            ch = self.getChar();
            e = self.getElement(ch)
            if e != 'chapter':
                raise RuntimeError('Bad Root' + e)
            while e != "/chapter":
                ch = self.getChar()
                e = self.getElement(ch)
                self.processState(e)
        elif state == 'number':
            self.chapNum,ch = self.getNum()
            e = self.getElement(ch)
            if e != '/number':
                raise RuntimeError('expected "/number')
            return True
#        elif state == 'outline':
        else:
            raise RuntimeError('unknown state: ' + state);
                
    def run(self, state):
        self.processState(state)
#        str = " "
#        while len(str) > 0:
#            str = self.fh.readline()
#            if len(str) > 0:
#                self.T.insert(END,str)
#        self.fh.close() 
        
# main program
print (chr(12))
print('Started basic_e_book')
xml = DoXML('Chapter_02.xhtml')
xml.run('INIT') 

fh.close()
mainloop()
