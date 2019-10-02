# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:44:18 2019

@author: Ben Adziashvili
"""


def doXinrange():
    dict={}
    for x in range(5):
        dict[x]=x*x
    return dict
    


def main():
    x=doXinrange()
    print (x)

if __name__ == '__main__':
    main()