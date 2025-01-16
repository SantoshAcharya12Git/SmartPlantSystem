Smart Plant Monitoring IoT System
This project is a Smart Plant Monitoring System that uses a Raspberry Pi 4 as a Flask server, a DHT11 sensor for temperature and humidity, a soil moisture sensor, and an Arduino for client-side data collection. The data is visualized using ThingSpeak.

## Components
- **Raspberry Pi 4**: Acts as the server running a Flask application.
- **DHT11 Sensor**: Measures temperature and humidity.
- **Soil Moisture Sensor**: Measures the moisture level of the soil.
- **Arduino**: Collects data from the sensors and sends it to the Flask server.
- **ThingSpeak**: Used for data visualization.

## Features
- Real-time monitoring of soil moisture, temperature, and humidity.
- Data visualization on ThingSpeak.
- Alerts and notifications based on sensor readings.

## Setup

### Hardware
**Connect the DHT11 Sensor:**
- VCC to 5V
- GND to GND
- Data to GPIO pin 5 on the Raspberry Pi

**Connect the Soil Moisture Sensor:**
- VCC to 5V
- GND to GND
- Analog output to A0 on the Arduino

**Connect the Arduino:**
- Connect the Arduino to the Raspberry Pi via USB.

### Software
**Clone the Repository:**

```bash
git clone <repository-url>
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Configure ThingSpeak:**
Update `THINGSPEAK_API_KEY` and `THINGSPEAK_CHANNEL_ID` in `santosh_smart_system.py` with your ThingSpeak credentials.

**Run the Flask Server:**

```bash
python santosh_smart_system.py
```

**Upload Arduino Code:**
Upload the Arduino code to your Arduino board to start sending data to the Flask server.

## Usage
- Access the Flask server on your Raspberry Pi's IP address at port 5000.
- Monitor the sensor data on ThingSpeak.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.


