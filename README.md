# Invisible-cloak

Color Detection and Background Replacement
Overview
This project utilizes OpenCV to perform color detection and replace a specified color (orange and purple in this case) in the video stream with a static background. It uses HSV color space for better color detection and performs morphological operations to refine the mask.

Project Structure
color_detection.py: Main script for capturing video, detecting specified colors, and replacing them with the background.
Prerequisites
Ensure you have the following installed:

Python 3.x
OpenCV
Numpy
You can install the required Python packages using the following command:

pip install opencv-python-headless numpy
How to Use
Running the Script
To run the color detection and background replacement, execute the following command:

python color_detection.py
Script Details
Capture Video: The script captures video from the default camera (index 0).
Background Initialization: The first 30 frames are used to capture the background image.
Color Detection: Colors within the orange and purple ranges are detected in the video stream.
Background Replacement: Detected colors are replaced with the captured background.
Display: The script displays the original video, background, and various masks in separate windows.
Key Functions
cv2.VideoCapture(0): Captures video from the default camera.
cv2.inRange(): Creates a binary mask for specified color ranges in HSV space.
cv2.morphologyEx(): Applies morphological operations to refine the mask.
np.where(): Replaces detected colors with the background.
Exiting the Script
To exit the script and close all windows, press the 'q' key while the video is being displayed.

Example
When you run the script, you will see the following windows:

Display: The video stream with specified colors replaced by the background.
background: The static background image.
mask01: Mask for the orange color range.
mask02: Mask for the purple color range.
combined_mask: Combined mask for both color ranges.
Acknowledgements
OpenCV for computer vision functionalities.
Numpy for numerical operations.


