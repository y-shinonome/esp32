import network, machine, socket, re, pwm
ESSID = 'esp32'
PASSWORD = '12345678'
IP = '192.168.5.1'
       
ap = network.WLAN(network.AP_IF)
ap.config(essid=ESSID, authmode=3, password=PASSWORD)
ap.ifconfig((IP,'255.255.255.0',IP,'8.8.8.8'))
ap.active(True)  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def home_page(cmd):
  html = '<html>\
  <head>\
  <meta name="viewport" content="width=device-width, initial-scale=1">\
  </head>\
  <body>\
  <p>' + cmd + '</p>\
  <form method="GET">\
  <input type="submit" name="cmd" value="1">\
  </form>\
  <form method="GET">\
  <input type="submit" name="cmd" value="2">\
  </form>\
  <form method="GET">\
  <input type="number" name="duty">\
  <input type="submit" name="cmd" value="3">\
  </form>\
  </body>\
  </html>'
  return html

while True:
  conn, addr = s.accept()
  request = str(conn.recv(1024)).lower()
  m = re.search(r'cmd=(\d)', request)

  cmd = ''

  if m != None :
    cmd = m.group(0)
    if cmd == 'cmd=1':
      pwm.wot()
    elif cmd == 'cmd=2':
      pwm.neutral()
    elif cmd == 'cmd=3':
      m = re.search(r'duty=(\d+)', request)
      if m != None :
        duty = m.group(0)
        duty = re.search(r'(\d+)', duty).group(0)
        pwm.ctrl(int(duty))

  response = home_page(cmd)
  conn.send(response)
  conn.close()