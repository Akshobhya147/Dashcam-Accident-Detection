import cv2
import einops
import numpy as np
import remotezip as rz
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras import layers
import pandas as pd
import os

ni=0
data=[]



def load_videos_and_labels(video_dir, csv_path, num_frames=50, frame_size=(224, 224)):
    """
    Loads videos, extracts frames, and matches them with labels from a CSV file.

    Args:
        video_dir (str): Path to the directory containing video files.
        csv_path (str): Path to the CSV file containing video filenames and labels.
        num_frames (int): Number of frames to extract per video.
        frame_size (tuple): Resize frames to this size (height, width).

    Returns:
        A list of tuples (frames, label), where:
        - frames: Tensor of shape (num_frames, frame_height, frame_width, 3).
        - label: Corresponding label for each set of frames.
    """
    print('new callll')
    # Load labels from CSV
    df = pd.read_csv(csv_path)

    # List to store each set of frames and its label
    # for _, row in df.iterrows():
    for i in range(8):
        # video_path = os.path.join(video_dir, row['File Name'])
        x1=None
        global ni
        # x1=df.iloc(ni+i)
        try:
          x1=df.iloc[ni]
        except:
          print('ohho')
          return
        print(type(x1))
        print('Video:',x1['File Name'])
        video_path=os.path.join(video_dir,x1['File Name'])

        label = x1['Class']
        # print('Video:',x1['File Name'])

        # Capture the video
        cap = cv2.VideoCapture(video_path)
        frames = []

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)

        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                break
            # Resize the frame
            frame = cv2.resize(frame, frame_size)
            # Convert BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)


        cap.release()

        if len(frames) == num_frames:
            frames = np.array(frames, dtype=np.float32) / 255.0  # Normalize frames
            global data
            data.append((frames, label))

        ni+=1
    return

# Here, I am using existing videos for testing. However, real-time camera feed can also be used.
video_dir = 'normal'
csv_path = 'datasheet_new.csv'
load_videos_and_labels(video_dir, csv_path)

dts=[]
for p in data:
    dts.append({"A":p[0].tolist(),"B":int(p[1])})
dts
type(dts[0]["A"])


import requests
import numpy as np
import json
from twilio_messaging import message
# Generate example data
data_to_send = dts

# Endpoint URL
url = "Your ngrok server URL"


try:
	print("sending data")
	response = requests.post(url, json=data_to_send, verify=False,timeout=12000)
	
	print("Status Code:", response.status_code)
	_json=response.json()
	print("Response:", _json)
	if(_json["ground_truth"]):
		#Accident
		#Get coordinates from GPS sensor
		sample_coordinates="latitude,longitude"
		
		google_maps_uri="https://www.google.com/maps/place/"+sample_coordinates
		
		#Get driver's details from config
		sample_driver_name="John Doe"
		
		message_body=sample_driver_name+" has likely been in an accident.\nPlease find their current loacation here: "+google_maps_uri
		
		message(_to="Contact number",_body=message_body)
		
    
except requests.exceptions.RequestException as e:
    print("Request error:", e)
