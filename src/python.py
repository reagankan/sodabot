import os, sys
from wallaby import *
#from botball import *
from constants import JOINT

def move_forward():
    print("Hello world")
    """
    motor(0, 100)
    msleep(5000)
    ao()
    """

    print("press R button to start\n");
    """
    while(digital(13) ==0){
    msleep(20);
    """
    print("Connecting\n");
    create_connect(); # this engages the create
    while(get_create_lbump()==0 and get_create_rbump()==0):
        create_drive_direct(100,100);
        msleep(100);
    print("Button Hit\n");
    create_stop();
    create_disconnect();
    msleep(500);

def menu():
    print("========Menu=========")
    print("1. move forward")
    print("2. move arm")
    return raw_input("Enter 1 or 2.")

def move_arm():
    mav(JOINT.zero, 100)
    msleep(2000)
    ao()

def main():
    choice = None
    valid_choice = ["1", "2"]
    while choice not in valid_choice:
        choice = menu()

    if choice is "1":
        print("choice 1: move forward")
        move_forward()
    elif choice is "2":
        print("choice 2: move arm")
        move_arm()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    move_arm()
    #main()



