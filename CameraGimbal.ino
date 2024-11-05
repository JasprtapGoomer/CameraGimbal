#include <ESP32Servo.h>

Servo horizontalServo;  // Controls left-right movement
Servo verticalServo;    // Controls up-down movement

const int horizontalPin = 18;  // GPIO pin for horizontal servo
const int verticalPin = 19;    // GPIO pin for vertical servo

void setup() {
  Serial.begin(115200);
  
  // Attach the servos to the specified pins
  horizontalServo.attach(horizontalPin);
  verticalServo.attach(verticalPin);

  // Initialize both servos to center position
  horizontalServo.write(90);  // Center for horizontal (left-right)
  verticalServo.write(90);    // Center for vertical (up-down)
}

void loop() {
  if (Serial.available() > 0) {
    // Read the command from the serial input
    String command = Serial.readStringUntil('\n');
    
    // Check the command format (e.g., "H,90" or "V,45")
    if (command.length() > 2 && command[1] == ',') {
      char servoType = command[0];          // First character ('H' or 'V')
      int angle = command.substring(2).toInt();  // Extract angle from command

      // Control the horizontal servo (left-right)
      if (servoType == 'H' && angle >= 0 && angle <= 180) {
        horizontalServo.write(angle);
        Serial.print("Horizontal servo set to angle: ");
        Serial.println(angle);
      }
      // Control the vertical servo (up-down)
      else if (servoType == 'V' && angle >= 0 && angle <= 180) {
        verticalServo.write(angle);
        Serial.print("Vertical servo set to angle: ");
        Serial.println(angle);
      } else {
        Serial.println("Invalid command or angle out of range.");
      }
    }
  }
}
