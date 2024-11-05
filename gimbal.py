import cv2
import serial
import time

# Serial connection to the ESP32
serial_port = '/dev/cu.usbserial-11430'  # Update this to your actual port
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

# Initialize webcam
cap = cv2.VideoCapture(0)  # Default webcam, change if using a different ID
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load the pre-trained Haar Cascade for face detection
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize variables for servo control
frame_center_x = 320  # X-center of the frame
servo_angle = 90      # Start with the servo centered
tolerance = 50        # Increase tolerance to reduce small adjustments

def send_horizontal_angle(angle):
    # Ensure the angle is within 0 to 180 and send it to the ESP32
    if 0 <= angle <= 180:
        command = f"H,{angle}\n"
        ser.write(command.encode())
        print(f"Sent horizontal command: {command.strip()}")
def send_vertical_angle(angle):
    # Ensure the angle is within 0 to 180 and send it to the ESP32
    if 0 <= angle <= 180:
        command = f"V,{angle}\n"
        ser.write(command.encode())
        print(f"Sent horizontal command: {command.strip()}")

try:
    send_horizontal_angle(90)
    send_vertical_angle(80)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # Find the largest face as the main subject
            (x, y, w, h) = max(faces, key=lambda rect: rect[2] * rect[3])
            face_center_x = x + w // 2

            # Calculate the horizontal movement needed
            offset_x = face_center_x - frame_center_x

            # Adjust the servo angle based on the face position
            if abs(offset_x) > tolerance:
                adjustment = int(offset_x / 50)
                servo_angle -= adjustment
                servo_angle = max(0, min(servo_angle, 180))
                send_horizontal_angle(servo_angle)

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
