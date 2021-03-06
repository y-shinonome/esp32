import network, machine, socket, html, request, _thread, time
from GY271 import GY271
from Motor import Motor

ESSID = 'esp32'
PASSWORD = '12345678'
IP = '192.168.5.1'

gy271 = GY271()
motor = Motor()

ap = network.WLAN(network.AP_IF)
ap.config(essid=ESSID, authmode=3, password=PASSWORD)
ap.ifconfig((IP,'255.255.255.0',IP,'8.8.8.8'))
ap.active(True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

stopTime = time.time()
def motorController(drivingTime):
  try:
    global stopTime
    stopTime = time.time() + drivingTime
    while time.time() < stopTime:
      motor.drive(gy271.directionalDifference())
      time.sleep_ms(5)
  finally:
    motor.stop()

def stopMotor():
  global stopTime
  stopTime = time.time()

def resetDevice():
  gy271 = GY271()
  motor = Motor()

while True:
  conn, addr = s.accept()
  cmd, drivingTime, smallCoefficient, largeCoefficient, maxDuty_ns = request.parse(str(conn.recv(1024)).lower())
  if cmd == 1:
    gy271.calibration()
  elif cmd == 2:
    gy271.setDirection()
  elif cmd == 3:
    motor.configure(drivingTime, smallCoefficient, largeCoefficient, maxDuty_ns)
    _thread.start_new_thread(motorController, (drivingTime, ))
  elif cmd == 4:
    stopMotor()
  elif cmd == 5:
    resetDevice()

  response = html.contents(gy271, motor, drivingTime)
  conn.send(response)

  conn.close()