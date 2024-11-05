# Gimbal Tracking Project

This project implements a gimbal system designed to keep a person centered in the video frame, adjusting for movement. The system includes Arduino code for servo control and a Python script for tracking and stabilization.

## Project Structure

- **CameraGimbal.ino**: Arduino code for controlling the gimbal servos based on input data.
- **gimbal.py**: Python script for detecting a person in the frame and sending control signals to the gimbal to maintain their centered position.

## Features

- **Real-Time Tracking**: Tracks a person in the video frame and adjusts the camera’s position to keep them centered.
- **Servo Control**: Controls two servos to move the camera smoothly in both horizontal and vertical directions.
- **UART Communication**: Uses UART for communication between the Arduino and the Python script to relay control signals.

## Getting Started

### Prerequisites

- Arduino IDE for uploading `CameraGimbal.ino`.
- Python 3 and OpenCV library for running `gimbal.py`.

### Hardware Requirements

- ESP32 Wrover Cam module for video capture and control.
- Logitech C920x HD Pro webcam (or similar) for video input.
- Two servos for gimbal control.

### Installation

1. **Arduino Setup**:
   - Connect your ESP32 and upload the `CameraGimbal.ino` code using the Arduino IDE.
   
2. **Python Setup**:
   - Install necessary Python packages:
     ```bash
     pip install opencv-python
     ```
   - Run the `gimbal.py` script to start tracking and controlling the gimbal.

### Usage

1. Ensure all connections are secure, and power on the system.
2. Run the `gimbal.py` script on your computer. This initializes tracking and communicates with the ESP32 for gimbal movement.
3. As the person moves within the frame, the gimbal adjusts to keep them centered automatically.

### Files

- **CameraGimbal.ino**: Contains the code for servo movements and UART communication.
- **gimbal.py**: Contains the tracking logic and sends commands to the gimbal.

### Contributing

Feel free to contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License.

