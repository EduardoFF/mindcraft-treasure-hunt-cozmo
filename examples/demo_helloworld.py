#!/usr/bin/env python3

'''
Makes cozmo saying "hello world"
'''

from mindcraft_treasure_hunt_cozmo import *

def cozmo_program():
    say_text("Hello world")
    
run_on_cozmo_with_viewer(cozmo_program)
