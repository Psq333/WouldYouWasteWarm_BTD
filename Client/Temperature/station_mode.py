import network
import urequests          # library used for making HTTP requests
import time
import json

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
  print('connecting to network...')
  wlan.connect('Pasquale-pc', 'Pasquale')
  while not wlan.isconnected():
    pass
print('network config:', wlan.ifconfig())




