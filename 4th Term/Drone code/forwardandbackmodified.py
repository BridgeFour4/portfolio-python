from pyparrot.Bebop import Bebop
import math

# you will need to change this to the address of YOUR mambo
bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

if (success):
    # get the state information
    print("sleeping")
    bebop.smart_sleep(2)
    bebop.ask_for_state_update()
    bebop.smart_sleep(2)

    print("taking off!")
    bebop.safe_takeoff(5)
    bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=1)
    
    bebop.smart_sleep(3)

    print("Flying direct: going forward (positive pitch)")
    bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=3.4)
    
    bebop.smart_sleep(5)
    bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=.5)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=1)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1)
    bebop.smart_sleep(2)
    bebop.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=.5)
    
    bebop.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=3)
    
    #bebop.smart_sleep(3)
    #print("flipping")
    #bebop.flip("front")

    print("landing")
    bebop.safe_land(5)
    bebop.smart_sleep(5)

    print("disconnect")
    bebop.disconnect()