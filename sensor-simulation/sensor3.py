import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=cst8916iot.azure-devices.net;DeviceId=sensor_NAC;SharedAccessKey=cWuJkWHWOGpspUPxXgL9rRbmTKo/P2+W/4e/7QGOHlo="

def get_telemetry():
    return {
        "location": "NAC",
        "iceThickness": random.uniform(0.0, 30.0),
        "surfaceTemperature": random.uniform(-20.0, 20.0),
        "snowAccumulation": random.uniform(0.0, 30.0),
        "externalTemperature": random.uniform(-20.0, 20.0),
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