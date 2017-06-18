#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, time
print('\t \t  WELCOME TO TEMPERATURE SENSOR PANEL')
print('\n' * 2)        
        

# function: read and parse sensor data file
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
    if(path == "/sys/bus/w1/devices/28-0000075694cd/w1_slave"):
      print ('Sensor 1:  '+ str(value))
    elif(path=="/sys/bus/w1/devices/28-0215012254ff/w1_slave"):
      print('Sensor 2:  '+ str(value))
      print('_________________')
      print('\n')
      
  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e
  return value

# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/28-0000075694cd/w1_slave",
  "/sys/bus/w1/devices/28-0215012254ff/w1_slave"
)

# read sensor data
data = 'N'
for i in range(1000000):
  for path in pathes:
    data += ':'
    
    data += read_sensor(path)
    time.sleep(0.15)
  

