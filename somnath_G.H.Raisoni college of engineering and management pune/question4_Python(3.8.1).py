#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:49:37 2021

@author: samac
"""


def subStringsStartingHere(string, n,
                           startIndex):
    count = 0
    i = startIndex + 1
     
    while(i <= n) :
        if string.startswith(
                 string[startIndex : i]):
            count += 1
        else :
            break
         
        i += 1
     
    return count
 
def countSubStrings(string, n) :
    count = 0
     
    for i in range(n) :

        if string[i] == string[0] :
            count += subStringsStartingHere(
                              string, n, i)
     
    return count
 
 
if __name__ == "__main__" :
     
    string = input()
    n = len(string)
    print(countSubStrings(string, n))
