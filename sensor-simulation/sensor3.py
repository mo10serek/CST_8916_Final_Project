import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "Your IoT Hub device connection string here"

def get_telemetry():
    return {
        "location": "NAC",
        "iceThickness": random.uniform(0.0, 30.0),
        "surfaceTemperature": random.uniform(-20.0, 20.0),
        "snowAccumulation": random.uniform(0.0, 30.0),
        "externalTemperature": random.uniform(-20.0, 20.0),
        "timestamp": datetime.now()
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            data = get_telemetry()
            message = Message(str(data))
            client.send_message(message)
            print(f"Sent message: {message}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()