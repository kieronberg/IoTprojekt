import random
import time
import json
import ssl
from paho.mqtt import client as mqtt

# MQTT / IoT Hub connection details (update as needed)
path_to_root_cert = "root_cert.pem"
device_id = "vehicle-001"
sas_token = "device-sas-token"       # If using Azure IoT Hub MQTT
iot_hub_name = "iot-hub-name"
mqtt_hub_hostname = "test.mosquitto.org"
mqtt_hub_port = 1883


def on_connect(client, userdata, flags, str(rc)):
    print("Device connected with result code:"+ str(rc))

def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code:", str(rc))

def on_publish(client, userdata, mid):
    print("Device sent message")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Topic subscribed!")

def on_message(client, userdata, msg):
    print("\nReceived message")
    print("Topic: '" + msg.topic+"', payload: " + str(msg.payload))

def generate_vehicle_data():

    # Simulating movement within a geographic bounding box
    latitude = random.uniform(49.0000, 54.5000)
    longitude = random.uniform(14.5000, 24.0800)

    speed = random.uniform(20, 120)         # km/h
    fuel_level = random.uniform(10, 100)    # %
    engine_temp = random.uniform(70, 110)   # °C

    payload = {
        "device_id": device_id,
        "gps": {"lat": latitude, "lon": longitude},
        "speed": speed,
        "fuel_level": fuel_level,
        "engine_temperature": engine_temp,
        "timestamp": time.time()
    }

    return payload

def simulate_vehicle_device():

    client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)

    # Register callbacks
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    # If using Azure IoT Hub MQTT:
    # client.username_pw_set(
    #     username=iot_hub_name + ".azure-devices.net/" +
    #     device_id + "/?api-version=2021-04-12",
    #     password=sas_token
    # )
    #
    # client.tls_set(
    #     ca_certs=path_to_root_cert,
    #     certfile=None,
    #     keyfile=None,
    #     cert_reqs=ssl.CERT_REQUIRED,
    #     tls_version=ssl.PROTOCOL_TLSv1_2,
    # )
    # client.tls_insecure_set(False)

    print("Connecting to MQTT broker...")
    client.connect(mqtt_hub_hostname, port=mqtt_hub_port)

    print("Connected.")

    # Standard MQTT device telemetry topic
    topic = f"vehicles/{device_id}/telemetry/"
    print("MQTT Topic:", topic)

    # Start sending simulated data
    while True:
        data = generate_vehicle_data()
        message = json.dumps(data)

        client.publish(topic, message, qos=1)
        print("Message sent:", message)

        time.sleep(10)   # publish interval


# Start simulating the device
simulate_vehicle_device()
