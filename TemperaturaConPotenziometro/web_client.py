

import network
import urequests          # library used for making HTTP requests
import time
import json
import machine


stuff = 'home1_internal_temp'
value = 0
url = 'http://192.168.137.100:8081/'
dato_precedente = 0

while True:
    #if(nuovo valore != value) allora aggiorna
    adc = machine.ADC(0)
    pot_value = adc.read()
    tvolt = pot_value * 4.4 / 4095.0
    tempC = (tvolt - 0.5) * 100
    print(pot_value, "  ", tvolt, "  ", tempC)
    json_string = {'key' : stuff, 'value': tempC}
    if dato_precedente != tempC:
      #print(json.dumps(json_string).encode('utf-8'))
      response = urequests.post(url,data=json.dumps(json_string).encode('utf-8'))
      dato_precedente = tempC
    time.sleep(1)




