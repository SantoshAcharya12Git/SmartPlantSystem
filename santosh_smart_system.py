from flask import Flask, request
from grove.display.jhd1802 import JHD1802
from seeed_dht import DHT
import requests

app = Flask(__name__)

# Initialize the LCD
lcd = JHD1802()

# Initialize the DHT sensor (pin 5)
dht_sensor = DHT('11', 5)  # DHT11 sensor on GPIO5

# ThingSpeak configuration
THINGSPEAK_API_KEY = "793U8MCPJ7WD5JAP"
THINGSPEAK_CHANNEL_ID = "2809919"
THINGSPEAK_URL = f"https://api.thingspeak.com/update"

def send_to_thingspeak(temp, hum, moisture):
    """Send data to ThingSpeak."""
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temp,
        'field2': hum,
        'field3': moisture
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=payload)
        if response.status_code == 200:
            print("Data sent to ThingSpeak successfully.")
        else:
            print(f"Failed to send data to ThingSpeak: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")

@app.route('/update', methods=['GET'])
def update():
    # Get moisture value from the query parameters
    moisture = request.args.get('moisture')
    
    if moisture:
        try:
            moisture_value = int(moisture)
            print(f"Received moisture value: {moisture_value}")
            
            # Read temperature and humidity from DHT sensor
            hum, temp = dht_sensor.read()
            
            if hum is not None and temp is not None:
                # Clear the LCD
                lcd.clear()
                # Display temperature and humidity on the first row
                lcd.setCursor(0, 0)  # Set cursor to row 0, column 0
                lcd.write(f"Temp:{temp}C Hum:{hum}%")
                # Display moisture value on the second row
                lcd.setCursor(1, 0)  # Set cursor to row 1, column 0
                lcd.write(f"Moisture:{moisture_value}")
                
                # Send data to ThingSpeak
                send_to_thingspeak(temp, hum, moisture_value)
            else:
                # Display error messages if DHT sensor readings fail
                lcd.clear()
                lcd.setCursor(0, 0)
                lcd.write("DHT Sensor Error")
                lcd.setCursor(1, 0)
                lcd.write("Check Connections")
        except ValueError:
            print("Invalid moisture value received.")
            lcd.clear()
            lcd.setCursor(0, 0)
            lcd.write("Invalid Data")
            lcd.setCursor(1, 0)
            lcd.write("Check Sender")
    else:
        print("No moisture value received.")
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.write("No Data Received")
        lcd.setCursor(1, 0)
        lcd.write("Awaiting Input")
    
    return 'Data Received'

if __name__ == '__main__':
    # Start the Flask web server
    app.run(host='0.0.0.0', port=5000)