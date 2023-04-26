
## Additional Project Components
### Fire detection

Fire detection of this project is for fire fighting purposes. So we considered a way to accurately detect fire through two sensors and then find the coordinate value of the fire.

The fire detection system determines that the fire was truly detected when object detection by the camera sensor and fire wavelength detection by the flame sensor were performed at the same time.

* Object Detection

The project contains object detection by using darknet yoloV4-tiny. 
I made customize weight file by machine learning. 
It learned about 4000 times for 2 classes. 
I extracted the coordinate value of fire by extracting the coordinate of the bounding box drawn when detecting fire.
And i modified batch and subdivision for Jsons capability.



* Fire wavelength detection

A flame sensor is detect a specific wavelength generated only fire.(185nm~260nm) It can detect up to flame of in front 0.5m(50cm)
  
  
* System only Fire Detection  

  <img src = https://github.com/yongscode/Fire-Detected-by-two-senser-/blob/main/data.PNG>
                                           < System operation when a fire is detected>
  
  
  
  1.The flame ahead is detected by two sensors at same time.
  
  2.fire_detection.ino sends pyserial value to  detect_demo.py for notify fire detection by flame sensor
  
  3.At same time, detect_demo.py is calculation coordinate Bounding Box of Fire
  
  4.Detect_fire() in detect_demo.py returns the x,y coordinates of the fire and the string 'fire detected' after inspecting whether the flame has been detected by two  sensors.
  
  5.test.py receives a coordinate of fire coordinate and a string 'fire detected' from detect_fire() imported from detect_fire().
  
  6.If the coordinate value >0, that the fire has been detected.
  
 
