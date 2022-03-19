from machine import PWM, Pin
from time import time, sleep_ms

pwmLeft = PWM(Pin(0), freq=200, duty_ns=1000000)
pwmRight = PWM(Pin(2), freq=200, duty_ns=1000000)

SMALL_COEFFICIENT = 200000
LARGE_COEFFICIENT = 400000
MAX_DUTY_NS = 1750000
MIN_DUTY_NS = 1000000

def drive(drivingTime, gy271):
  stopTime = time() + int(drivingTime)

  while time() < stopTime:
    leftPulseWidth, rightPulseWidth = pulseWidth(gy271.directionalDifference())
    pwmLeft.duty_ns(leftPulseWidth)
    pwmRight.duty_ns(rightPulseWidth)

    print(str(gy271.directionalDifference()) + ',' + str(pwmLeft.duty_ns()) + ',' + str(pwmRight.duty_ns()))
    sleep_ms(5)

  pwmLeft.duty_ns(MIN_DUTY_NS)
  pwmRight.duty_ns(MIN_DUTY_NS)

def pulseWidth(theta):
    if theta >= 0:
      leftPulseWidth = (MAX_DUTY_NS - (round(theta * SMALL_COEFFICIENT)))
      rightPulseWidth = (MAX_DUTY_NS - (round(theta * LARGE_COEFFICIENT)))
    elif theta < 0:
      leftPulseWidth = (MAX_DUTY_NS + (round(theta * LARGE_COEFFICIENT)))
      rightPulseWidth = (MAX_DUTY_NS + (round(theta * SMALL_COEFFICIENT)))

    if leftPulseWidth < MIN_DUTY_NS:
      leftPulseWidth = MIN_DUTY_NS
    
    if rightPulseWidth < MIN_DUTY_NS:
      rightPulseWidth = MIN_DUTY_NS

    return (leftPulseWidth, rightPulseWidth)