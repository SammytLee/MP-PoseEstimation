# MP-PoseEstimation
## Introduction
This is a project in pose estimation through mediapipe. 
It shows and labels different landmarks and explores the capabailities on videos found from open source videos from pexel. 
Some projects include using distances between points to show change in movement.

## Technology
* Python 3.9
* Mediapipe 0.8.5
* OpenCV-Python 4.5.2.54
* numpy 1.20.3
## Launch
Simply run the program and it should launch using the video specified in the code.

## Features
### AiTrainerProject
This project is a curl trainer. It uses a video a person curling and then creates a count based on a completion of a curl. 
It recognizes the curl through angle and distance between two points found using landmarks in the pose detection algorithm.
It imports the pose module.

### AwesomePoseProject
This project uses a video and captures and shows some of the landmarks and how it follows the image in real time. 
Written is a fps counter and a highlight on the landmark that is associated with the right elbow.

### PoseEstimationMin
This project is written to show where the landmarks are located on a video. It uses a video from pexel.
This is written as a stand alone program and doesn't have modularity.

### PoseModule
This project creates different functions that can be acessed through other projects. It is used for the AiTrainer and the AwesomePoseProject.
#### findPose
This part of the program finds landmarks and and can draw them on the image or video
#### findPosition
This finds the positions of the landmarks and their corresponding id.
#### findAngle
this finds the angle that is created between two landmarks and returns the angle.
## Project Status
completed

## Sources
This is an exercise project from freeCodeCamp.org on youtube. https://www.freecodecamp.org/news/advanced-computer-vision-with-python/
