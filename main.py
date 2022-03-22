import network, machine, socket, html, request
from GY271 import GY271
from MOTOR import MOTOR

ESSID = 'esp32'
PASSWORD = '12345678'
IP = '192.168.5.1'

gy271 = GY271()
motor = MOTOR()

ap = network.WLAN(network.AP_IF)
ap.config(essid=ESSID, authmode=3, password=PASSWORD)
ap.ifconfig((IP,'255.255.255.0',IP,'8.8.8.8'))
ap.active(True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

while True:
  conn, addr = s.accept()
  cmd, drivingTime, smallCoefficient, largeCoefficient, maxDuty_ns = request.parse(str(conn.recv(1024)).lower())
  print(cmd)
  if cmd == 1:
    gy271.calibration()
  elif cmd == 2:
    gy271.setDirection()
  elif cmd == 3:
    motor.configure(drivingTime, smallCoefficient, largeCoefficient, maxDuty_ns)
    motor.drive(gy271)

  response = html.contents(gy271, motor)
  conn.send(response)

  conn.close()