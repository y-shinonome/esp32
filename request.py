import re

def parse(request):

  cmd = 0
  drivingTime = 0   

  m = re.search(r'favicon.ico', request)

  if m != None:
    return (cmd, drivingTime)

  m = re.search(r'cmd=(\d)', request)

  if m != None:
    if m.group(0) == 'cmd=1':
      cmd = 1
    elif m.group(0) == 'cmd=2':
      cmd = 2
    elif m.group(0) == 'cmd=4':
      cmd = 4
      m = re.search(r'drivingtime=(\d*)', request)
      if m != None:
        m = re.search(r'\d+$', m.group(0))
        if m != None:
          drivingTime = int(m.group(0))
    elif m.group(0) == 'cmd=5':
      cmd = 5
      m = re.search(r'drivingtime=(\d*)', request)
      if m != None:
        m = re.search(r'\d+$', m.group(0))
        if m != None:
          drivingTime = int(m.group(0))

  return (cmd, drivingTime)