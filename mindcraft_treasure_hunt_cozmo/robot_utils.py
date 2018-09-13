import time
from . import mindcraft


def pause(time_in_seconds):
    """**Pause for certain amount of time in seconds**
    
    :param time_in_seconds: time to pause
    :type time_in_seconds: float
    """
    time.sleep(time_in_seconds)
    
def abort():
    """**Abort the entire program execution**
    """
    print("Aborting program...")
    raise SystemExit

def set_volume_high():
    mindcraft._mycozmo.set_robot_volume(1)
def set_volume_low():
    mindcraft._mycozmo.set_robot_volume(.05)
def set_volume_med():
    mindcraft._mycozmo.set_robot_volume(.5)
    
    
def enable_head_light():
    """**Enable head light to see in low light conditions**
    """

    mindcraft._mycozmo.set_head_light(True)
def disable_head_light():
    """**Disable head light**
    """

    mindcraft._mycozmo.set_head_light(False)

