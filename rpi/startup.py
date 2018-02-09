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
		
		cmd = ["python", "/home/pi/Desktop/meesh_ttmode.py"]
		subprocess.call(cmd)
	else:
		#runs hacktooth script
		
		subprocess.check_call(["/home/pi/hello-world.sh"])

except:
	GPIO.cleanup()
