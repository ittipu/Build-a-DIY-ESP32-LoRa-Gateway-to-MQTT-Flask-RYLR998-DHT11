from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

# Initialize Flask and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lora_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# --- MQTT Configuration ---
MQTT_BROKER = "mqtt.iotbhai.io"  # The free public broker we used in the ESP32 code
MQTT_PORT = 1883
MQTT_TOPIC = "iotbhai/lora_weather" # Make sure this matches your ESP32 code!

# --- MQTT Callbacks ---
def on_connect(client, userdata, flags, rc):
    print(f"✅ Connected to MQTT Broker! (Result code {rc})")
    client.subscribe(MQTT_TOPIC)
    print(f"📡 Listening for LoRa data on topic: {MQTT_TOPIC}")

def on_message(client, userdata, msg):
    try:
        # Decode the payload
        raw_payload = msg.payload.decode('utf-8')
        print(f"📥 Received JSON: {raw_payload}")
        
        # Parse the JSON string directly into a Python dictionary!
        data = json.loads(raw_payload)
        
        # Because the keys in our JSON perfectly match what the HTML dashboard
        # expects ('temp', 'humidity', 'rssi'), we just emit the whole dictionary!
        socketio.emit('new_data', data)
        
    except json.JSONDecodeError:
        print("⚠️ Error: Received message was not valid JSON.")

# --- Setup and Start MQTT ---
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to broker and start a background thread to listen for messages
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

# --- Flask Routes ---
@app.route('/')
def index():
    # This serves the beautiful HTML dashboard we built!
    return render_template('dashboard.html')

if __name__ == '__main__':
    print("🚀 Starting local web server...")
    print("👉 Open your browser and go to: http://127.0.0.1:5000")
    # Run the app with SocketIO
    socketio.run(app, debug=True)