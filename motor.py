from machine import PWM, Pin
from time import time, sleep_ms

pwm = PWM(Pin(0), freq=50, duty=50)

def drive(drivingTime, gy271):
  stopTime = time() + int(drivingTime)

  while time() < stopTime:
    pwm.duty(100 - (round(gy271.directionalDifference() * 12)))
    print(pwm.duty())
    sleep_ms(5)

  pwm.duty(50)

  while pwm.duty() != 50:
    pwm.duty(50)
    sleep_ms(100)
