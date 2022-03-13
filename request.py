import re

def parse(request):
  m = re.search(r'favicon.ico', request)

  if m != None:
    return None

  m = re.search(r'cmd=(\d)', request)

  if m != None:
    cmd = m.group(0)
    if cmd == 'cmd=1':
      return 1
    elif cmd == 'cmd=2':
      return 2
  
  return None