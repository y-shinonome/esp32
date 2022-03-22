from machine import PWM, Pin
from time import time, sleep_ms

class MOTOR():
  def __init__ (self):
    self.drivingTime = 0
    self.smallCoefficient = 200000
    self.largeCoefficient = 400000
    self.maxDuty_ns = 1750000
    self.minDuty_ns = 1000000
    self.pwmLeft = PWM(Pin(0), freq = 400, duty_ns = self.minDuty_ns)
    self.pwmRight = PWM(Pin(2), freq = 400, duty_ns = self.minDuty_ns)

  def drive(self, gy271):
    stopTime = time() + int(self.drivingTime)

    while time() < stopTime:
      leftPulseWidth, rightPulseWidth = self.pulseWidth(gy271.directionalDifference())
      self.pwmLeft.duty_ns(leftPulseWidth)
      self.pwmRight.duty_ns(rightPulseWidth)
      print(self.pwmLeft.duty_ns(), self.pwmRight.duty_ns())
      sleep_ms(5)
    
    while self.pwmLeft.duty_ns() != self.minDuty_ns or self.pwmRight.duty_ns() != self.minDuty_ns:
      self.pwmLeft.duty_ns(self.minDuty_ns)
      self.pwmRight.duty_ns(self.minDuty_ns)
      print(self.pwmLeft.duty_ns(), self.pwmRight.duty_ns())
      sleep_ms(5)

  def pulseWidth(self, radian):
    if radian >= 0:
      leftPulseWidth = (self.maxDuty_ns - (round(radian * self.smallCoefficient)))
      rightPulseWidth = (self.maxDuty_ns - (round(radian * self.largeCoefficient)))
    elif radian < 0:
      leftPulseWidth = (self.maxDuty_ns + (round(radian * self.largeCoefficient)))
      rightPulseWidth = (self.maxDuty_ns + (round(radian * self.smallCoefficient)))

    if leftPulseWidth < self.minDuty_ns:
      leftPulseWidth = self.minDuty_ns
    
    if rightPulseWidth < self.minDuty_ns:
      rightPulseWidth = self.minDuty_ns

    return (leftPulseWidth, rightPulseWidth)

  def configure(self, drivingTime, smallCoefficient, largeCoefficient, maxDuty_ns):
    self.drivingTime = drivingTime
    self.smallCoefficient = smallCoefficient
    self.largeCoefficient = largeCoefficient
    self.maxDuty_ns = maxDuty_ns