#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

MAXCOLOR = 8

msg = """
Control Your Robot!
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity (~ 1.2 m/s)
a/d : increase/decrease angular velocity (~ 1.8)

space key, s : force stop

c : Change RGB led Rainbow color
RED = 0,        // red
GREEN,          // green
BLUE,           // blue
YELLOW,         // yellow
PURPLE,         // purple
CYAN,           // cyan
WHITE,          // white
ALL_OFF         // off(black)

CTRL-C to quit
"""

e = """
Communications Failed
"""

def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(target_linear_vel, target_angular_vel):
    return "linear vel:%0.2f\t angular vel:%0.2f" % (target_linear_vel,target_angular_vel)

def makeSimpleProfile(output, input, slop):
    if input > output:
        output = min( input, output + slop )
    elif input < output:
        output = max( input, output - slop )
    else:
        output = input

    return output

def constrain(input, low, high):
    if input < low:
      input = low
    elif input > high:
      input = high
    else:
      input = input

    return input

def checkLinearLimitVelocity(vel, min, max):
    vel = constrain(vel, min, max)

    return vel

def checkAngularLimitVelocity(vel, max):
    vel = constrain(vel, -max, max)
    return vel

def set_ledColor(intColor):
    pub.publish(intColor)

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('swcon_teleop')
    tf_prefix = rospy.get_param("~tf_prefix", "")
    print("tf_prefix:"+tf_prefix)
    max_lin_vel = rospy.get_param("~max_lin_vel") #swcon_MAX_LIN_VEL = 1.20
    min_lin_vel = rospy.get_param("~min_lin_vel")
    max_ang_vel = rospy.get_param("~max_ang_vel") #swcon_MAX_ANG_VEL = 1.80
    lin_vel_step_size = rospy.get_param("~lin_vel_step")    #LIN_VEL_STEP_SIZE = 0.05
    ang_vel_step_size = rospy.get_param("~ang_vel_step")    #ANG_VEL_STEP_SIZE = 0.1
    ang_vel_rev = rospy.get_param("~ang_vel_reverse")       #1 for reversed
    pub = rospy.Publisher(tf_prefix+'/cmd_vel', Twist, queue_size=10)
    ledpub = rospy.Publisher('/rgbled', Int16, queue_size=4)

    status = 0
    target_linear_vel   = 0.0
    target_angular_vel  = 0.0
    control_linear_vel  = 0.0
    control_angular_vel = 0.0
    colorIdx = 0

    try:
        print(msg)
        while(1):
            key = getKey()
            if key == 'w' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel + lin_vel_step_size, min_lin_vel, max_lin_vel)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
            elif key == 'x' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel - lin_vel_step_size, min_lin_vel, max_lin_vel)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
            elif key == 'a' :
                if ang_vel_rev == 1:
                    target_angular_vel = checkAngularLimitVelocity(target_angular_vel - ang_vel_step_size, max_ang_vel)    
                else:
                    target_angular_vel = checkAngularLimitVelocity(target_angular_vel + ang_vel_step_size, max_ang_vel)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
            elif key == 'd' :
                if ang_vel_rev == 1:
                    target_angular_vel = checkAngularLimitVelocity(target_angular_vel + ang_vel_step_size, max_ang_vel)
                else:
                    target_angular_vel = checkAngularLimitVelocity(target_angular_vel - ang_vel_step_size, max_ang_vel)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
            elif key == ' ' or key == 's' :
                target_linear_vel   = 0.0
                control_linear_vel  = 0.0
                target_angular_vel  = 0.0
                control_angular_vel = 0.0
                print(vels(target_linear_vel, target_angular_vel))

            elif key == 'c' :                
                print("Color Enum:", colorIdx)
                ledpub.publish(colorIdx)
                colorIdx += 1
                if colorIdx == MAXCOLOR:
                    colorIdx = 0

            else:
                if (key == '\x03'):
                    break

            if status == 20 :
                print(msg)
                status = 0

            twist = Twist()

            control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (lin_vel_step_size/2.0))
            twist.linear.x = control_linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0

            control_angular_vel = makeSimpleProfile(control_angular_vel, target_angular_vel, (ang_vel_step_size/2.0))
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = control_angular_vel

            pub.publish(twist)

    except:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)

    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)