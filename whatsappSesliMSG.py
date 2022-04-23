# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:03:14 2022

@author: LENOVO
"""

import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:

    print("tekrar Dinleniyor..")
    audio = r.record(source,duration=5)
    try:
        str=r.recognize_google(audio, language="tr-tr")
        mesaj=str
       
    except:
            print("hata")
          


import pywhatkit as kit
try : 
    kit.sendwhatmsg("mesaj atılacak numara",mesaj,saat,dakika)
    print("oldu")
except : 
    print("hata")