import os, sys
from time import sleep
from omxplayer import OMXPlayer
from random import shuffle
import RPi.GPIO as GPIO
import os

directory = ""
my_path = "/home/pi/Desktop/Music"
pwr_pin = 18
play_pause_pin = 23
skip_pin = 22
louder_pin = 6
quieter_pin = 12
commands = {"play_pause": False,
                "stop": False,
                "quieter": False,
                "louder": False,
                "skip": False,
            "quit": False}
quit_pin = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(pwr_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(play_pause_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(skip_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(louder_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(quieter_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(quit_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(pwr_pin, GPIO.HIGH)

prev_butt_status = GPIO.input(quit_pin)
butt_status = prev_butt_status

def do_play_pause(pin_num):
    print("pressed play")
    sleep(0.5)

def do_quit(pin_num):
##    global butt_status
##    if butt_status == prev_butt_status:
##        print("yes")
##    butt_status = GPIO.input(pin_num)
##    sleep(0.5)
    print("y")

          
def do_skip(pin_num):
    print("pressed skip")

def do_quieter(pin_num):
    print ("pressed quieter")
    sleep(0.5)

def do_louder (pin_num):
    print ("pressed louder")
        

GPIO.add_event_detect(play_pause_pin, GPIO.RISING)
GPIO.add_event_detect(skip_pin, GPIO.RISING)
GPIO.add_event_detect(quieter_pin, GPIO.RISING)
GPIO.add_event_detect(louder_pin, GPIO.RISING)
GPIO.add_event_detect(quit_pin, GPIO.RISING, callback=do_quit, bouncetime=500)
# GPIO.add_event_callback(quit_pin, do_quit, bouncetime=500)
GPIO.add_event_callback(play_pause_pin, do_play_pause)
GPIO.add_event_callback(skip_pin, do_skip)
GPIO.add_event_callback(quieter_pin, do_quieter)
GPIO.add_event_callback(louder_pin, do_louder)

while True:
    try:
        print("I'm true")
        sleep(5)
    except:
        GPIO.cleanup()
        break
