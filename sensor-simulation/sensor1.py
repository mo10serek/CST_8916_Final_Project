import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=cst8916iot.azure-devices.net;DeviceId=sensor_Dow's_Lake;SharedAccessKey=ara6mlKIT/Lg6rWL2darl52NWAp90t8+B0EgrBWCtaw="

# This function is usually to send the query string to the Iot hub. This contains all the data that need to be send such as location, ice thickness, surface temperature, snow accumulation, and external temperature. The values are randomized to the realistic min and max values of each input.
def get_telemetry():
    return {
        "location": "Dow's Lake",
        "iceThickness": random.uniform(0.0, 30.0),
        "surfaceTemperature": random.uniform(-20.0, 20.0),
        "snowAccumulation": random.uniform(0.0, 30.0),
        "externalTemperature": random.uniform(-20.0, 20.0)
    }

# This function is where you connect to the Iot hub and send the quere string.
def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING) # get the connection to the Iot hub

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            data = get_telemetry() # get the data from the get_telemetry function
            message = Message(str(data)) # convert the data to a message object
            client.send_message(message) # send the message object to the client
            print(f"Sent message: {message}")
            time.sleep(10) # give 10 seconds duration
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect() # disconnect from the Iot hub if the user stop running

if __name__ == "__main__":
    main()