#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:49:51 2021

@author: samac
"""

def minc(mat):
    n=len(mat)
    m=len(mat[0])
 
    dist = int(n) + int(m) - 1
    mx = 0
    for i in range(n):
        for j in range(m):
            mx = max(mx,mat[i][j])
 
    freq = [[0 for i in range(mx + 1)]
               for j in range(dist)]
 
 
    for i in range(dist):
        for j in range(mx + 1):
            freq[i][j] = 0
 
 
    for i in range(n):
        for j in range(m):
 
            freq[i + j][mat[i][j]] += 1
 
    res = 0
    for i in range(dist // 2):
 
        maximum = 0
        tot = 0
 
        for j in range(mx + 1):
            maximum = max(maximum,
                          freq[i][j] +
                          freq[n + m - 2 - i][j])
 
            tot += (freq[i][j] +
                             freq[n + m - 2 - i][j])
 
        res += tot - maximum
 
    return res

def main():
    n,m=map(int,input().split(" "))
    mat=[]
    for i in range(n):
        m=input().split()
        mat.append([ord(i) for i in m])
    
    print(minc(mat))
    
    
main()
