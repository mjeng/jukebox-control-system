import subprocess
import RPi.GPIO as GPIO
from time import sleep

TT_pin = 17
pwr_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwr_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(TT_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(pwr_pin, GPIO.HIGH)
butt_status = GPIO.input(TT_pin)
try: 
	if butt_status:
		#runs TT mode
		print ("TTMODE")
	else:
		#runs hacktooth script
		print ("BLUTEOOTH")

except:
	GPIO.cleanup()
