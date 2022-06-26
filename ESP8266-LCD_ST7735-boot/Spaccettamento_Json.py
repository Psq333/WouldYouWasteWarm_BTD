






import urequests
#import prequests
import json
import time
import screen
#json = urequests.get(url = 'https://api.thingspeak.com/channels/1745453/feed/last')
fields_list = {
  'field2' : 11,
  'field3' : 10,
  'field4' : 0,
  'field5' : 0,
  'field6' : 0,
  'field7' : 0,
  'field8' : 0,
}




def chiamata_thinksSpeak():
  while True:
    cambio = False
    json = urequests.get(url = 'https://api.thingspeak.com/channels/1745453/feed/last')
    for i in range(2,9):
      fields = "field"+str(i) 
      valore_iniziale = json.text.find(fields) + 9
      valore_finale = 0
      while json.text[valore_iniziale + valore_finale] != '\"':
        valore_finale = valore_finale + 1
        time.sleep(0.1)
      json_sub = json.text[valore_iniziale:valore_iniziale+valore_finale]
      if json_sub != fields_list[fields]:
        fields_list.update({fields: json.text[valore_iniziale:valore_iniziale+valore_finale]})
        cambio = True
    if cambio:
      screen.Aggiornamento_Dati(fields_list)
    time.sleep(1)
    
  
  
  






