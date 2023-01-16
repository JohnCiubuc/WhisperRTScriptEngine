#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:44:45 2023

@author: inathero
"""
import urllib.request 
import webbrowser
search = ['search for', 'you search', 'google']
class WhisperRT_ScriptEngine:
    
    def __init__(self):
        print()
    def processIntent(self, text):
        base_text = text
        text = text.lower()
        # This is so basic, I'm so sorry
        # Search:
        for s in search:
            if s in text:
                n = text.index(s)
                textn=base_text[n+len(s)+1:]
                webbrowser.open("https://www.google.com/search?q="+urllib.parse.quote(textn))
                return
                
            
            