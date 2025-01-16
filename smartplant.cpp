#include <WiFi.h>

const int buzzerPin = 8;         // Buzzer connected to pin 8
const int moistureSensorPin = A0;  // Moisture sensor connected to pin A0
int moistureValue = 0;            // Variable to store the moisture level
int threshold = 400;              // Threshold for moisture level

// WiFi Credentials
const char* ssid = "Three_7AD76E";    //  WiFi SSID
const char* password = "2vLuswu235z3256";  //  WiFi password

// Raspberry Pi server IP and port
const String serverIp = "192.168.0.196"; // Raspberry Pi IP address
const int port = 5000;                   // Port for the Raspberry Pi web server

WiFiClient client;

void setup() {
  Serial.begin(9600);          // Start serial communication for debugging
  pinMode(buzzerPin, OUTPUT);  // Set buzzer pin as an output
  
  // Connect to WiFi
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  moistureValue = analogRead(moistureSensorPin);  // Read the moisture sensor value

  // Turn buzzer on or off based on moisture level
  if (moistureValue < threshold) {
    digitalWrite(buzzerPin, HIGH);  // Turn the buzzer on
  } else {
    digitalWrite(buzzerPin, LOW);   // Turn the buzzer off
  }

  // Send data to Raspberry Pi if WiFi is connected
  if (WiFi.status() == WL_CONNECTED) {
    if (client.connect(serverIp.c_str(), port)) {
      String url = "/update?moisture=" + String(moistureValue);
      client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                   "Host: " + serverIp + "\r\n" + 
                   "Connection: close\r\n\r\n");

      Serial.println("Data sent successfully");
      client.stop();
    } else {
      Serial.println("Connection failed");
    }
  }

  delay(2000);  // Wait for 2 seconds before sending again
}