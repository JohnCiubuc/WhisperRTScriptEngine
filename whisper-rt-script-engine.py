#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:44:45 2023

@author: inathero
"""
import urllib.request  
search = ['search for', 'you search', 'google']
class WhisperRT_ScriptEngine:
    
    def __init__(self):
        print()
    def processIntent(self, text):
        # This is so basic, I'm so sorry
        # Search:
        for s in search:
            if s in text:
                n = text.index(s)
                textn=text[n+len(s)+1:]
                urllib.request.urlopen("https://www.google.com/search?q="+textn)
                return
                
            
            