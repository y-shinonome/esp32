from machine import PWM, Pin
from time import sleep_ms

pwm = PWM(Pin(0))
pwm.freq(50)
pwm.duty(50)

def wot():
    for dutyRatio in range(pwm.duty() , 101, 1):
      pwm.duty(dutyRatio)
      sleep_ms(50)

def neutral():
  for dutyRatio in range(pwm.duty() , 49, -1):
    pwm.duty(dutyRatio)
    sleep_ms(50)

def ctrl(targetValue):
  if targetValue > pwm.duty():
    step = 1
  else:
    step = -1

  for dutyRatio in range(pwm.duty() , targetValue + step, step):
    pwm.duty(dutyRatio)
    sleep_ms(50)

def off():
  pwm.duty(0)

def output():
  print(pwm)