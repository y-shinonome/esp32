from machine import PWM, Pin
from time import time, sleep_ms

pwmLeft = PWM(Pin(0), freq=200, duty_ns=1000000)
pwmRight = PWM(Pin(2), freq=200, duty_ns=1000000)

SMALL_COEFFICIENT = 200000
LARGE_COEFFICIENT = 400000
MAX_DUTY_ns = 1750000
MIN_DUTY_ns = 1000000

def drive(drivingTime, gy271):
  stopTime = time() + int(drivingTime)

  while time() < stopTime:
    leftPulseWidth, rightPulseWidth = pulseWidth(gy271.directionalDifference())
    pwmLeft.duty_ns(leftPulseWidth)
    pwmRight.duty_ns(rightPulseWidth)
    sleep_ms(5)

  pwmLeft.duty_ns(MIN_DUTY_ns)
  pwmRight.duty_ns(MIN_DUTY_ns)

def pulseWidth(radian):
  if radian >= 0:
    leftPulseWidth = (MAX_DUTY_ns - (round(radian * SMALL_COEFFICIENT)))
    rightPulseWidth = (MAX_DUTY_ns - (round(radian * LARGE_COEFFICIENT)))
  elif radian < 0:
    leftPulseWidth = (MAX_DUTY_ns + (round(radian * LARGE_COEFFICIENT)))
    rightPulseWidth = (MAX_DUTY_ns + (round(radian * SMALL_COEFFICIENT)))

  if leftPulseWidth < MIN_DUTY_ns:
    leftPulseWidth = MIN_DUTY_ns
  
  if rightPulseWidth < MIN_DUTY_ns:
    rightPulseWidth = MIN_DUTY_ns

  return (leftPulseWidth, rightPulseWidth)