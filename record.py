# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 00:19:01 2023

@author: petersdorf
"""

import PIL.ImageGrab
import pytesseract as pt
from pytesseract import Output
import time
from datetime import datetime
import pytz
import pandas

pt.pytesseract.tesseract_cmd = r'C:\Users\BL16\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


while True:
    im = PIL.ImageGrab.grab(bbox =(100, 208, 205, 238), include_layered_windows=True)
    #im.show()
    image_data = pt.image_to_data(im, output_type=Output.DICT)
    pressure = image_data['text'][-1]
    
    im2 = PIL.ImageGrab.grab(bbox =(140, 318, 195, 340), include_layered_windows=True)
    #im2.show()
    image_data2 = pt.image_to_data(im2, output_type=Output.DICT)
    temperature = image_data2['text'][-1]
    
        
    im3 = PIL.ImageGrab.grab(bbox =(100, 370, 205, 400), include_layered_windows=True)
    #im.show()
    image_data3 = pt.image_to_data(im3, output_type=Output.DICT)
    location = image_data3['text'][-1]
    
    time_japan = pytz.timezone('Japan') 
    now = datetime.now(time_japan)
    print(pressure)
    print(temperature)
    print(location)
    print(now)
    df = pandas.DataFrame()
    df["time"] = [str(now)]
    df["pressure"] = [str(pressure)]
    df["location"] = [str(location)]
    df["temperature"] = [str(temperature)]
    df.to_csv("tracking_fr121d62dppc_nrw.dat", sep="\t", mode='a', header=False, index = False)
