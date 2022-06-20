import network
import urequests          # library used for making HTTP requests
import time
import json


stuff = 'home1_room1_radiator1'
value = 0
url = 'http://192.168.137.252:8081/'

while True:
    #if(nuovo valore != value) allora aggiorna
    json_string = {'key' : stuff, 'value': value}
    #print(json.dumps(json_string).encode('utf-8'))
    response = urequests.post(url,data=json.dumps(json_string).encode('utf-8'))
    time.sleep(1)


