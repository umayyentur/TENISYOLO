# TENNIS MATCH ANALYSIS AND TRACKING SYSTEM

This repository contains a computer vision system that analyzes tennis match videos. It detects players and the ball, tracks movements, measures shot speeds, and visualizes data on a mini-court overlay. The project demonstrates advanced techniques in object detection (YOLO-based), court line detection, and performance analysis, making it a valuable tool for match statistics and player insights.


## Project Overview

The main objective of this project is to provide comprehensive tracking and analysis of tennis matches. By leveraging player and ball detection models, the system can determine shot speeds, track player positions, and present the results using an augmented video output and statistical summaries. This information can be used to study player performance, improve strategies, or simply gain deeper insights into the match dynamics.


## Before and After

### Before
![Before](/input_vid/image.png)

### After
![After](output_vid/after.png)

The system processes the input video to detect players, the ball, and court lines, then overlays tracking information, speed statistics, and a mini-court view onto the output video.


## Features

1. **Player and Ball Detection**  
   Utilizes YOLO-based object detection models to accurately identify and locate players and the ball in each frame.

2. **Court Line Detection**  
   Predicts and marks the tennis court keypoints, enabling geometric transformations and mini-court visualization.

3. **Tracking and Interpolation**  
   - Tracks players and the ball across consecutive frames.  
   - Interpolates missing ball positions to handle occasional detection failures.

4. **Shot Analysis**  
   - Detects shot moments throughout the match.  
   - Measures ball speeds (km/h) and player movement speeds, providing a detailed performance breakdown.

5. **Mini-Court Visualization**  
   - Maps player and ball positions onto a scaled-down court.  
   - Offers a clear, real-time perspective of match flow and positioning.

6. **Statistical Analysis**  
   - Calculates average shot speeds and movement speeds.  
   - Enables deeper insights into player performance over the course of the match.

7. **Video Output**  
   - Draws bounding boxes, overlays court lines, and annotates speeds.  
   - Saves the processed video file in the `output_vid/` directory for easy review.

---

## Dependencies
pip install opencv-python pandas torch torchvision ultralytics

These dependencies cover computer vision functionalities, data handling, and the YOLO-based detection models.


### How to Run

1.Place your input video in the input_vid/ directory (e.g., input_video.mp4).

2.Run the main script with the following command:
python main.py

3.The processed output video will be saved as output_vid.avi in the output_vid/ directory.



Model Requirements

Ensure the following trained models are available in the models/ directory:
Player Detection Model: yolov8x.pt
Ball Detection Model: last.pt
Court Detection Model: Kyp_model.pth
If any model is missing or a .partial file is present, re-download the model for proper execution.


### Notes

*   Model Availability: Check that yolov8x.pt, last.pt, and Kyp_model.pth are correctly placed.
*   Incomplete Downloads: If you find a .partial file for a model, re-download to avoid issues.
*   System Requirements: A CUDA-capable GPU is recommended for faster processing of frames.



### Conclusion
This Tennis Match Analysis and Tracking System provides an end-to-end solution for extracting detailed statistics from tennis match footage. By combining cutting-edge object detection and motion analysis techniques, the system offers valuable insights into player performance, shot patterns, and match dynamics. The visual overlays and mini-court representation further enhance the ability to review and optimize play strategies.