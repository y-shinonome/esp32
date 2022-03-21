import network, machine, socket, html, request, motor, motorTest
from GY271 import GY271

ESSID = 'esp32'
PASSWORD = '12345678'
IP = '192.168.5.1'

gy271 = GY271()

ap = network.WLAN(network.AP_IF)
ap.config(essid=ESSID, authmode=3, password=PASSWORD)
ap.ifconfig((IP,'255.255.255.0',IP,'8.8.8.8'))
ap.active(True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

while True:
  conn, addr = s.accept()
  cmd, drivingTime = request.parse(str(conn.recv(1024)).lower())

  if cmd == 1:
    gy271.calibration()
  elif cmd == 2:
    gy271.setDirection()
  elif cmd == 4:
    motor.drive(drivingTime, gy271)
  elif cmd == 5:
    motorTest.drive(drivingTime, gy271)

  response = html.contents(gy271)
  conn.send(response)

  conn.close()