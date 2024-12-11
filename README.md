This repository is the aftermath of my university minor project, "Smart Dashcam". Smart Dascam is a safety system which uses multiple sensors and a machine learning model to detect collisions in real-time and contacts emergency contact based upon the severity of the accident.
The dataset for training the model was obtained from https://github.com/Cogito2012/CarCrashDataset.
The model I used is a cutom implementation of Resnet18 with the convolution layers replaced by (2+1)D Spatiotemporal convolutions.
Sensors and Modules used:
 - Neo-6M GPS module
 - SIM 800A GSM module
 - VL53L0X LIDAR sensor
 - Collision detection switch

To implement the model for inferencing on edge (RaspberryPi 4B), I used NGROK service to convert my colab TPU v28 runtime to a server, and made API calls by sending video data.

References:
https://www.tensorflow.org/tutorials/video/video_classification
https://arxiv.org/abs/1711.11248v3

https://youtu.be/r5snUkeDi-w

Peace out.
