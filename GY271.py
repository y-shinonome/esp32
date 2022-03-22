# in the implementation the following reference codes were used
#https://github.com/juliantesla13/micropython-esp32-qmc5883/blob/master/QMC5883.py

from math import sqrt, acos
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
    self.targetDirectionX = 0
    self.targetDirectionY = 0
    self.directionDegrees = 0

    self.i2c = I2C(scl = Pin(SCL), sda = Pin(SDA), freq = 400000)
    self.i2c.start()
    #Write Register 0BH by 0x01 (Define Set/Reset period)
    self.i2c.writeto_mem(ADDR, 0xB, b'\x01')
    #Write Register 09H by 0x1D 
    #(Define OSR = 512, Full Scale Range = 2 Gauss, ODR = 200Hz, set continuous measurement mode)
    self.i2c.writeto_mem(ADDR, 0x9, b'\x1101')
    self.i2c.stop()

    #Reserve some memory for the raw xyz measurements.
    self.data = array('B', [0] * 9)

  def read(self):
    #performs a reading of the data in the position of momoria 0x00, by means of a buffer
    data = self.data

    self.i2c.readfrom_mem_into(ADDR, 0x00, data)
    sleep_ms(5)

    x = unpack('<h', bytes([data[0], data[1]]))[0] - self.offsetX 
    y = unpack('<h', bytes([data[2], data[3]]))[0] - self.offsetY

    return (x, y)
  
  def calibration(self):
    maxX = 0
    minX = 0
    maxY = 0
    minY = 0
    
    for i in range(1500):
      x, y = self.read()
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
    x, y = self.read()

    self.targetDirectionX = x
    self.targetDirectionY = y

  def directionalDifference(self):
    currentDirectionX, currentDirectionY = self.read()

    targetVectorLength = sqrt((self.targetDirectionX ** 2) + (self.targetDirectionY ** 2))
    currentVectorLength = sqrt((currentDirectionX ** 2) + (currentDirectionY ** 2))

    dotProduct = (self.targetDirectionX * currentDirectionX) + (self.targetDirectionY * currentDirectionY)

    if dotProduct == 0:
      return 0
    elif targetVectorLength == currentVectorLength:
      return 0
      
    theta = acos(dotProduct / round(targetVectorLength * currentVectorLength))

    crossProduct = (currentDirectionX * self.targetDirectionY) - (currentDirectionY * self.targetDirectionX)

    if crossProduct < 0:
      theta = theta * -1

    return theta