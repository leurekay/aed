# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:16:40 2018

@author: zee
"""

import serial  
import os
import time
  
  
#n = t.write('you are my world')  
#print t.portstr  
#print n  
#str = t.read(n)  
#print str  

N=4
aed_id='#'
monitor='1'
display='0'


def oneSet(aed_id,monitor,display):
    ser = serial.Serial('com3',115200)
    save_name=os.path.join('data2','%s-m%s-d%s.txt'%(aed_id,monitor,display)) 
    already_file=0
    while os.path.exists(save_name):
        already_file+=1
        save_name=os.path.join('data2','%s-m%s-d%s.txt'%(aed_id+'~'+str(already_file),monitor,display)) 
        
    print ('start collect data,it will be saved in %s'%save_name)
    
    if display==0 or display=='0':
        print ('you should calibration in 90 s firstly!!!')
        calibration_s=time.time()
        while True:
            line=ser.readline() 
            if '*C,66&' in line:
                print (line)
                print ('calibration done!!!\nsleep 90s')
                time.sleep(90)
                
                break
            if (time.time()-calibration_s)>90:
                print ('No calibration!!!!\nWe had waited 90 s')
                break
    
    box=[]
    count=0
    while True:
        
        line = ser.readline() 
        box.append(line)
        print (line)        
        if 'UART Data:*B' in line:
            count+=1

        if count==N:
            txt=''
            for row in box:
                txt+=row
            with open(save_name,'w') as f:
                f.write(txt)
            break
    ser.close()


while True:
    print ('======================================================================')
    input_aed=raw_input('AED_ID(%s):'%aed_id)
    if input_aed!='':
        aed_id=input_aed
        
        
    input_monitor=raw_input('Monitor(%s):'%monitor)
    if input_monitor!='':
        monitor=input_monitor
        
    input_display=raw_input('True display statue(%s):'%display)
    if input_display!='':
        display=input_display
    
    oneSet(aed_id,monitor,display)
    
    