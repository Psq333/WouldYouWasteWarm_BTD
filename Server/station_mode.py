import network

def connection():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('Pasquale-pc', 'Pasquale')
    while not wlan.isconnected():
      pass
    wlan.ifconfig(('192.168.137.100', '255.255.255.0', '192.168.137.1', '192.168.137.1'))
  print('network config:', wlan.ifconfig())
  return wlan.ifconfig()[0] 
