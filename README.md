# Aruco-markers
---

# Aruco Marker Detection and Generation

Welcome to the Aruco Marker Detection and Generation repository! This repository provides code and resources for generating and detecting Aruco markers using Python and OpenCV. Aruco markers are widely used in computer vision for tasks like camera pose estimation, augmented reality, and robotics.

## Project Overview

This repository includes:

- **Marker Generation:** Scripts to generate Aruco markers with different sizes and IDs.
- **Marker Detection:** Code to detect and decode Aruco markers in images or video streams.
- **Pose Estimation:** Example code for estimating the camera's pose relative to detected markers.

## Technologies Used

- **Python 3.x**
- **OpenCV (with the Aruco module)**
- **Numpy** (for matrix operations)

## Installation

Before running the code, make sure to install the required Python packages:

```bash
pip install opencv-python opencv-contrib-python numpy
```

The `opencv-contrib-python` package includes the `aruco` module, which is essential for working with Aruco markers.

## Usage

### 1. Marker Generation

You can generate Aruco markers using the `generate_aruco_marker.py` script. The script allows you to specify the marker dictionary, ID, and size.

Example:

```python
import cv2
import cv2.aruco as aruco

# Define the dictionary used to generate Aruco markers
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

# Generate the marker with a specific ID
marker_id = 0
marker_size = 200  # Size in pixels
marker = aruco.drawMarker(aruco_dict, marker_id, marker_size)

# Save the marker image
cv2.imwrite(f'aruco_marker_{marker_id}.png', marker)
```

This will generate and save a marker with the specified ID and size.

### 2. Marker Detection

To detect Aruco markers in an image or video, use the `detect_aruco_marker.py` script. The script will identify and decode markers, drawing their outlines and displaying the detected IDs.

Example:

```python
import cv2
import cv2.aruco as aruco

# Load the image or video stream
image = cv2.imread('image_with_markers.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize the Aruco dictionary and parameters
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

# Detect the markers
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

# Draw the detected markers
aruco.drawDetectedMarkers(image, corners, ids)

# Display the result
cv2.imshow('Aruco Markers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 3. Pose Estimation

The repository also includes an example of how to estimate the camera's pose relative to detected Aruco markers.

## Examples

Aruco markers detection pics:
![image](https://user-images.githubusercontent.com/91476640/199065641-aeff7251-70ea-4b76-8498-39fcaf2f8d90.png)




Aruco Markers pose display pics:
![image](https://user-images.githubusercontent.com/91476640/199068110-bfae4caa-3416-4768-8029-443d36eea36b.png)

## Contributions

Feel free to fork this repository, submit issues, or make pull requests. Contributions are welcome!

## Contact

For any questions or feedback, please reach out at mahata2657@gmail.com.

---



