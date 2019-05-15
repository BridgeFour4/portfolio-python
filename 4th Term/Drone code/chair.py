from pyparrot.Bebop import Bebop
import math

# you will need to change this to the address of YOUR mambo
bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect

if (success):
    # get the state information
    print("sleeping")
    bebop.smart_sleep(2)
    bebop.ask_for_state_update()
    bebop.smart_sleep(5)

    print("taking off!")
    bebop.safe_takeoff(5)
    bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=1)
    
    bebop.smart_sleep(3)

    print("Flying direct: going forward (positive pitch)")
    bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=2.2)
    
    bebop.smart_sleep(3)
    # moving up through the middle of the chair
    bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=.75)
    bebop.smart_sleep(3)
    #moving left
    bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=1.5)
    bebop.smart_sleep(3)
    #go back
    bebop.smart_sleep(3)
    bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1.4)
    bebop.smart_sleep(3)
    #moving right
    bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1.2)
    bebop.smart_sleep(3)
    
    bebop.smart_sleep(3)
    bebop.flip(direction="front")
    bebop.smart_sleep(3)
    print("landing")
    bebop.safe_land(5)
    bebop.smart_sleep(5)

    print("disconnect")
    bebop.disconnect()