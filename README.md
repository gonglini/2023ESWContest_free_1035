# Detect & Extinguish Fire Servies (Self-driving fire truck)

This project is created for 21th 2023embedded SW contest by undergraduates attending Suwon, Kyungil Univ. 
<img src = https://github.com/gonglini/Embedded_sw_contest_2023/assets/65767592/36d6ebdd-c0c3-4b90-a59a-4096cc5b802d.jpeg width="450" height="350" align="right">


## Overview
This project is the source code for self-Driving fire Truck. This code implements motion control of a 1:8 scale car, including move by joystick or autonomatically. Supporting libraries provide additional capabilities, such as object detection by camera to provide accident. The software is implemented on a Jetson Nano running Ubuntu 18.04 with ROS Melodic installed.

The software is composed of Arduino, C++ and Python nodes in a ROS framework.


## Software settings
```
* Jetpack 4.5.1 / Darknet yoloV4 / ROS Melodic
* OpenCV 4.5.1 / CUDA 10.0 / CUDNN 8.0 / Tensorflow 2.5.0
```
I used compact command to install ROS melodic written by zeta(https://github.com/zeta0707/installROS.git)

## Software Flow
  <img src = https://github.com/gonglini/Embedded_sw_contest_2023/assets/65767592/531eb7bb-9086-449d-bdcc-fade2fef8485.jpg  height="360" >

## Self Driving

Self-driving is for patrol where being fired. We used python to send goal for ROS SLAM. Cartogrphor is also used to obtain maps.

Here's the map and the navigation we got.

  <img src = https://user-images.githubusercontent.com/65767592/235427299-fb32638c-17a3-4ed7-bec6-ed2805b5473b.gif  width="435" height="350"  align="left">
  <img src = https://user-images.githubusercontent.com/65767592/235427736-1006aaee-7dc9-47ca-af52-d081794774f0.jpg   width="370" height="350" align="right">
    
    
## Fire detection  

|  Darknet YoloV4  | IR sensor  |
|---|---|
|The project contains object detection by using darknet yoloV4-tiny. We made customize weight file by machine learning.  We extracted the coordinate value of fire by extracting the coordinate of the bounding box drawn when detecting fire.And i modified batch and subdivision for Jsons capability.   |  Fire detection of this project is for fire fighting purposes.  So we considered a way to accurately detect fire through two sensors and then find the coordinate value of the fire.  The fire detection system determines that the fire was truly detected when object detection by the camera sensor and fire wavelength detection by the flame sensor were performed at the same time.  A flame sensor is detect a specific wavelength generated only fire.(185nm~260nm) It can detect up to flame of in front 1.5m |


## Fire extinguisher (Robot Arm)
<p align="center"><img src = https://github.com/gonglini/Embedded_sw_contest_2023/assets/65767592/15f0531c-172c-4d51-a259-3555f71480d0.gif width="700" height="300"  ></p>    
The fire extinguish system is processed by the Robot arm. When the fire was detected, they get a position where the fire was caused.    

After extinguishing system got position from the jetson, the water pump  will execute the Robot arm which is included.    
We used a Dinamixel actuator AX-12 with a U2D2 module.
 
    
## Application

  <img src = https://github.com/gonglini/Embedded_sw_contest_2023/assets/65767592/98005e97-6d1a-4589-a7d7-dc19c0718fd5.gif  width="350" height="350"  align="right">

One of the important things is we had to know where and when the fire occurred.  
So our team also made an application for users.   
When the fire occurred, An application announce fire to the user that the situation happened.   
After, it announces that the robot extinguishes the fire and where it occurred The application is connected by wifi with ESP8266.    
They communicate by Web using the GET method.    
It runs as a client While ESP8266 as Server.    
Here are how the application is processed.    
