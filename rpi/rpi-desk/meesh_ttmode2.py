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
##quit_pin = 0
commands = {"play_pause": False,
                "stop": False,
                "quieter": False,
                "louder": False,
                "skip": False,
                    "quit":False}
print(commands)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwr_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(play_pause_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(skip_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(louder_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(quieter_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
##GPIO.setup(quit_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(pwr_pin, GPIO.HIGH)


def create_playlist():
        print(os.getcwd())
        print(os.chdir(my_path))
        print(os.getcwd())
        my_music = os.listdir(my_path)
        return my_music
def do_play_pause(pin_num):
        commands["play_pause"] = True
def do_quit(pin_num):
    commands["quit"] = True
def do_quieter(pin_num):
    commands["quieter"] = True
def do_louder(pin_num):
    commands["louder"] = True
def do_skip(pin_num):
        print("skip pressed")
        commands["skip"] = True
    
def basic_func():
##        try:
                print(commands)
                print(commands["play_pause"])
                directory = create_playlist()
                shuffle(directory)
                print ("currently, my playlist is {}".format(directory))
                my_playlist_length = len(directory)
                my_song_index = 0
                my_song = directory[0]
                print ("My song right now is {}".format(my_song))
                player = OMXPlayer(my_song)
                print ("im intalized")
                player.pause()
                my_volume = player.volume()
                while True:

                        if player.position() >= player.duration()-1.5:
                                commands["skip"] = True
                        if commands["play_pause"]:
                                print("pressed")
                                if not player.is_playing():
                                    print ("I was paused, now I'm playing")
                                    player.play()
                                elif player.is_playing():
                                    player.pause()    
                                print (player.duration())
                                print (player.position())
                                commands["play_pause"] = False
                        elif commands["quit"]:
                                print ('im quiting')
                                commands["quit"] = False
                                player.quit()
                                break
                        elif commands["quieter"]:
                                my_volume = my_volume-1000
                                player.set_volume(my_volume)
                                print(my_volume)
                                commands["quieter"] = False
                        elif commands["louder"]:
                                my_volume = player.volume()
                                my_volume = my_volume+1000
                                player.set_volume(my_volume)
                                print(my_volume)
                                commands["louder"] = False
                        elif commands["skip"]:
                                player.quit()
                                my_song_index = (my_song_index + 1)%my_playlist_length
                                if my_song_index == 0:
                                        print ("my playlist was {}".format(directory))
                                        shuffle(directory)
                                        print ("my playlist is now {}".format(directory))
        
                                my_song = directory[my_song_index]
                                player = OMXPlayer(my_song)
                                player.set_volume(my_volume)
                                commands["skip"] = False
                                
                                print ("Now, my_song is {}".format(my_song))
                                

                
##        except:
                GPIO.cleanup()
                player.quit()


print (directory)
GPIO.add_event_detect(play_pause_pin, GPIO.RISING)
GPIO.add_event_detect(skip_pin, GPIO.RISING)
GPIO.add_event_detect(quieter_pin, GPIO.RISING)
GPIO.add_event_detect(louder_pin, GPIO.RISING)
##GPIO.add_event_detect(quit_pin, GPIO.RISING)
GPIO.add_event_callback(play_pause_pin, do_play_pause)
GPIO.add_event_callback(skip_pin, do_skip)
GPIO.add_event_callback(quieter_pin, do_quieter)
GPIO.add_event_callback(louder_pin, do_louder)
##GPIO.add_event_callback(quit_pin, do_quit)
basic_func()

