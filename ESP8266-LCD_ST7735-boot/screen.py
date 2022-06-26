
# MicroPython ST7735 TFT display driver example usage

from machine import Pin, SPI
from tft import TFT_GREEN
import time
import font

# DC       - RS/DC data/command flag
# CS       - Chip Select, enable communication
# RST/RES  - Reset
dc  = Pin(4, Pin.OUT)
cs  = Pin(2, Pin.OUT)
rst = Pin(5, Pin.OUT)
# SPI Bus (CLK/MOSI/MISO)
# check your port docs to see which Pins you can use
spi = SPI(1, baudrate=8000000, polarity=1, phase=0)

# TFT object, this is ST7735R green tab version
tft = TFT_GREEN(128, 160, spi, dc, cs, rst, rotate=90)

# init TFT
tft.init()
def inizializzazione():
    tft.clear(tft.rgbcolor(0, 0, 0)) #b, g, r
    tft.text(25,30,"Would you", font.terminalfont, tft.rgbcolor(255, 255, 105), 2)
    time.sleep(0.2)
    tft.text(38,30,"ould you", font.terminalfont, tft.rgbcolor(0,0,0), 2)
    tft.text(25,45,"Waste your", font.terminalfont, tft.rgbcolor(255, 255, 105), 2)
    time.sleep(0.2)
    tft.text(38,45,"aste your", font.terminalfont, tft.rgbcolor(0, 0, 0), 2)
    tft.text(25,60,"Warm?", font.terminalfont, tft.rgbcolor(255, 255, 105), 2)
    time.sleep(0.2)
    tft.text(38,60,"arm?", font.terminalfont, tft.rgbcolor(0, 0, 0), 2)
    tft.text(25,75,"?", font.terminalfont, tft.rgbcolor(255, 255, 105), 2)
    time.sleep(0.2)
    tft.text(25,30,"W", font.terminalfont, tft.rgbcolor(0,0,0), 2)
    tft.text(25,45,"W", font.terminalfont, tft.rgbcolor(0,0,0), 2)
    tft.text(25,60,"W", font.terminalfont, tft.rgbcolor(0,0,0), 2)
    tft.text(25,75,"?", font.terminalfont, tft.rgbcolor(0,0,0), 2)

    tft.text(40,50,"WWW?", font.terminalfont, tft.rgbcolor(255, 255, 105), 3)
    time.sleep(0.5)
    tft.text(40,50,"WWW?", font.terminalfont, tft.rgbcolor(0, 0, 0), 3)
    time.sleep(0.2)



#tft.pixel(127, 159, tft.rgbcolor(250,0,0))

