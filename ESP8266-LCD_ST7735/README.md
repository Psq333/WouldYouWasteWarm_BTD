# micropython-st7735-esp8266

Driver and examples to ST7735s display in ESP-8266-12E [Micropython](http://micropython.org/), originally written by [@hosaka](https://github.com/hosaka/).

### PINOUT



| TFT Display | Esp-8266 |
| :--: | :--: |
| GND | GND|
| VCC | VCC  3V|
| CS | D4 (GPIO2)|
| D/C | D2 (GPIO4)|
| RST | D1 (GPIO5)|
| SDA | D7 (GPIO13)|
| SCL | D5 (GPIO14)|
| BLK | VCC 3V|

![image](assets/images/ESP-8266-ST7735S.png)

### Changelog:
* Fixed SPI to always send Bytearrays
* Added Option to rotate Display

### Rotating
You can rotate the display by either 90, 180 or 270 degrees.
Rotating can be done when creating TFT Object
```python
tft = TFT_GREEN(width, height, spi, dc, cs, rst, rotate=90)
```
or during runtime
```python
tft.changeRotate(270)
```

### Example
`main.py` is an example program using the driver.
Configure the wifi of the esp by editing this line
`sta.connect("YOUR_SSID_HERE", "YOUR_PASSWORD_HERE")`
with your appropiate values. Then use netcat to connect to the esp on port 23:
`nc IP_OF_ESP 23`
You can now type any text and after hitting Enter the text will be displayed.
You can also rotate the display by sending e.g.
`rotation=270`

### Credits
Thanks to <a href="https://github.com/hosaka/">hosaka</a> who initially wrote the driver
