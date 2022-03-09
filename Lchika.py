from machine import Pin
import time

p2 = Pin(2, Pin.OUT)

def run():
  for i in range(10):
    p2.on()
    time.sleep_ms(500)
    p2.off()
    time.sleep_ms(500)