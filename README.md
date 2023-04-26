# Self-driving_fire-truck

This project was created by undergraduates attending Suwon, Kyungil Univ.

## Overview
This project is the source code for self-Driving fire Truck. This code implements motion control of a 1:8 sclae car, including move by joystick or autonomatically. Supporting libraries provide additional capabilities, such as object detection by camera to provide accident. The software is implemented on a Jetson Nano running Ubuntu 18.04 with ROS Melodic installed.

The software is composed of Arduino, C++ and Python nodes in a ROS framework.

#### Hardware:
The frame utilized is aluminum profile with acryl plate. 

Component List:
* Computer: Jetson Nano 4gb B01 
* MCU: ESP32 node32s
* Motors: 520 DC encoder motor
* Sensor: arduino fire detector 
* Lidar: Rplidar A1
* Actuator: Dinamixel
* Battery: 4s 1600 mAh Lipo
* other: XL4015 dc-dc stepdown converter, customized PCB etc..

#### Software:

Software version:
* Jetpack 4.5.1
* OpenCV 4.5.1
* CUDA 10.0
* CUDNN 8.0
* Tensorflow 2.5.0
* Darknet yoloV4
* ROS Melodic

I used compact command to install ROS melodic written by zeta(https://github.com/zeta0707/installROS.git)

**NOTE**  A SWAP partition of about 8 GB on the jetson sd card is necessary to increase the virtual memory available beyond the Jetsons onboard RAM. In my experience the catkin compilation process uses all the onboard RAM and stalls indefinitely and does not complete without adding a SWAP partition. Example instructions for adding a SWAP partition. 

## Fire detection

Fire detection of this project is for fire fighting purposes. So we considered a way to accurately detect fire through two sensors and then find the coordinate value of the fire.

The fire detection system determines that the fire was truly detected when object detection by the camera sensor and fire wavelength detection by the flame sensor were performed at the same time.

### Object Detection

The project contains object detection by using darknet yoloV4-tiny. 
I made customize weight file by machine learning. 
It learned about 4000 times for 2 classes. 
I extracted the coordinate value of fire by extracting the coordinate of the bounding box drawn when detecting fire.
And i modified batch and subdivision for Jsons capability.


### Fire wavelength detection

A flame sensor is detect a specific wavelength generated only fire.(185nm~260nm) It can detect up to flame of in front 0.5m(50cm)
  
  
### System only Fire Detection  

  <img src = https://github.com/yongscode/Fire-Detected-by-two-senser-/blob/main/data.PNG>
                                           < System operation when a fire is detected>
  

