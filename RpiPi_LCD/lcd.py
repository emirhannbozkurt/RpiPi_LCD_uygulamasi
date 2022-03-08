import drivers
from time import sleep

display = drivers.Lcd()

while True:
        
        display.lcd_display_string("Emirhan BOZKURT", 1) 
        display.lcd_display_string("M.Akif DOGAN", 2) 