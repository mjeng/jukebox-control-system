from pyomxplayer import OMXPlayer
import RPi.GPIO as GPIO
import time
import os
from random import shuffle

pwrPin = 18
playpausePin = 17

GPIO.setmode(GPIO, BCW)
GPIO.setup(pwrPin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(readPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(pwrPin, GPIO.HIGH)
about_to_toggle_pause = False
x = 0
i = 0

class dumb():
	def __init__(self, num):
		self.integer = num
	def make_playlist(path):
		temp = os.listdir(path)
		for name in temp:
			name2 = name.replace(" ", "")
			os.system("mv " + name + ".mp3 " + name2 + ".mp3 -i")
		temp2 = os.listdir(path)
		shuffle(temp2)
		return temp2

try:
	GPIO.add_event_detect(playpausePin, GPIO.RISING)
	player = OMXPlayer('/home/pi/Desktop/Music/' + temp2[i])
	player.toggle_pause()
	about_to_toggle_pause = False
	x = dumb(0)
	def play_pause(pin_num):
		y = x
		if y.integer == 0:
			y.integer = 1
			player.toggle_pause()
	def skip(pin_num):
		i = i + 1
		player = OMXPlayer('/home/pi/Desktop/Music/' + temp2[i])
	GPIO.add_event_callback(playpausePin, play_pause)
	while True:
		x.integer = 0
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	player.stop()