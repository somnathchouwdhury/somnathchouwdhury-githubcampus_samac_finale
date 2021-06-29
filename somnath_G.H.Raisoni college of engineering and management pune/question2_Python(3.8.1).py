#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:22:32 2021

@author: samac
"""

n= int(input())

A=list(map(int,input().split()))

tA=A[1:n-1]

print(max(tA))
