
import ssd1306
from machine import Pin
from machine import I2C
import time
# Heltec LoRa 32 with OLED Display
oled_width = 128
oled_height = 64
# OLED reset pin
i2c_rst = Pin(16, Pin.OUT)
# Initialize the OLED display
i2c_rst.value(0)
time.sleep_ms(5)
i2c_rst.value(1) # must be held high after initialization
# Setup the I2C lines
i2c_scl = Pin(15, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(4, Pin.OUT, Pin.PULL_UP)
# Create the bus object
i2c = I2C(scl=i2c_scl, sda=i2c_sda)
# Create the display object
def scrittura(ip, fields, new_data):
  oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
  oled.fill(0)
  oled.text('IP ', 0, 0)
  oled.text(ip , 0, 10)
  oled.text('Ex temp:   ' + str(fields['home1_external_temp']), 0, 25)
  oled.text('Int temp:   ' + str(fields['home1_internal_temp']), 0, 35)
  if new_data == True:
    oled.text('New data coming', 0, 45)
  else:
    oled.text('', 0, 45)
  '''if fields['home1_room1_radiator1'] == 1:
    oled.text('Rad 1:   Open', 0, 20)
  else:
    oled.text('Rad 1:   Close', 0, 20)
  if fields['home1_room1_radiator2'] == 1:
    oled.text('Rad 2:   Open', 0, 30)
  else:
    oled.text('Rad 2:   Close', 0, 30)
  if fields['home1_room1_window1'] == 1:
    oled.text('Win 1:   Open', 0, 40)
  else:
    oled.text('Win 1:   Close', 0, 40)
  if fields['home1_room1_window2'] == 1:
    oled.text('Win 2:   Open', 0, 48)
  else:
    oled.text('Win 2:   Close', 0, 48)
  if fields['home1_room1_window3'] == 1:
    oled.text('Win 3:   Open', 0, 55)
  else:
    oled.text('Win 3:   Close', 0, 55)'''

  oled.show()
  
  
  
def scritturaD():
  oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
  oled.fill(0)
  oled.text('Wait', 40, 25)
  oled.text('for internet', 15, 35)
  oled.show()






