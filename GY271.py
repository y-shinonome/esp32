from math import degrees, atan2 
from machine import Pin, I2C
from struct import unpack
from array import array
from time import sleep_ms

SDA = 21
SCL = 22
ADDR = 13

class GY271():
  def __init__ (self):
    self.offsetX = 0
    self.offsetY = 0
    self.direction = 0

    self.i2c =i2c= I2C(scl=Pin(SCL), sda=Pin(SDA), freq=400000)
    i2c.start()
    #Write Register 0BH by 0x01 (Define Set/Reset period)
    i2c.writeto_mem(ADDR, 0xB, b'\x01')
    #Write Register 09H by 0x1D 
    #(Define OSR = 512, Full Scale Range = 8 Gauss, ODR = 200Hz, set continuous measurement mode)
    i2c.writeto_mem(ADDR, 0x9, b'\x11101')
    i2c.stop()

    #Reserve some memory for the raw xyz measurements.
    self.data = array('B', [0] * 9)

  def read(self):
    #performs a reading of the data in the position of momoria 0x00, by means of a buffer
    data = self.data

    self.i2c.readfrom_mem_into(ADDR, 0x00, data)
    sleep_ms(5)

    x = unpack('<h', bytes([data[0], data[1]]))[0]   
    y = unpack('<h', bytes([data[2], data[3]]))[0]
    angle = degrees(atan2(y, x))

    return (x, y, angle)
  
  def calibration(self):
    maxX = 0
    minX = 0
    maxY = 0
    minY = 0
    
    for i in range(1500):
      x, y, angle =self.read()
      if maxX < x:
        maxX = x
      
      if minX > x:
        minX = x
      
      if maxY < y:
        maxY = y
      
      if minY > y:
        minY = y
      
      sleep_ms(2)
    
    self.offsetX = ((maxX + minX) / 2)
    self.offsetY = ((maxY + minY) / 2)

  def setDirection(self):
    self.direction = self.read()[2]