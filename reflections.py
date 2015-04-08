#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

# Ordered Raspberry Pi pins
pins = [ 4, 17, 27, 22 ];

# Fire pin (high voltage level) function
def firepin( param ):
  # Cool all the pins (low voltage level)
  for pin in pins:
    GPIO.output(pin, GPIO.LOW)
  currpin = pins[ param ]
  GPIO.output(currpin, GPIO.HIGH)

# Preparing Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
for pin in pins:
  GPIO.setup (pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

# Forth-back loop
curr = 0
dir  = +1
while True:
  firepin( curr )
  curr += dir
  if curr >= 3:
  	dir = -1
  if curr <= 0:
  	dir = +1
  time.sleep( 0.2 )