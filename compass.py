from QMC5883 import QMC5883L
import time
qmc=QMC5883L()

maxX = 0
minX = 0
maxY = 0
minY = 0

def r():
  while 1 :
    x, y, z, angle =qmc.read()
    print (angle)
    time.sleep_ms(100)

def calibration():
  global maxX
  global minX
  global maxY
  global minY
  
  for i in range(1500):
    x, y, z, angle =qmc.read()
    if maxX < x:
      maxX = x
    
    if minX > x:
      minX = x
    
    if maxY < y:
      maxY = y
    
    if minY > y:
      minY = y
    
    time.sleep_ms(1)

  print(str(maxX) + ',' + str(minX) + ',' + str(maxY) + ',' + str(minY) + ',' + str((maxX + minX) / 2) + ',' + str((maxY + minY) / 2))

def offset():
  print(str(maxX) + ',' + str(minX) + ',' + str(maxY) + ',' + str(minY) + ',' + str((maxX + minX) / 2) + ',' + str((maxY + minY) / 2))