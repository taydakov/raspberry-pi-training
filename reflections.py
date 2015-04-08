#!/usr/bin/env python

import time

def action( param ):
  print param

curr = 1
dir  = +1
while True:
  action(curr)
  curr += dir
  if curr >= 4:
  	dir = -1
  if curr <= 1:
  	dir = +1
  time.sleep(0.2)