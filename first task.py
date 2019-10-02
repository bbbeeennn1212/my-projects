  
    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def createdict():
    dict = {}
    for x in range(3):
        key= input (" please input the key")
        dict[key] = int(input(" please enter the value(integer)"))
    return dict 


def check(dict):
    y=input(" please enter a key")
    if y in dict:
        print ("yes")
    else:
        print ("no")
    return
    
    
def main():
    x=createdict()
    check(x)
    
    

if __name__ == '__main__':
    main()
