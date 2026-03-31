# Build a DIY ESP32 LoRa Gateway to MQTT & Flask | RYLR998 & DHT22

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Platform](https://img.shields.io/badge/platform-ESP32-green.svg) ![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![Flask](https://img.shields.io/badge/framework-Flask-black.svg)

This repository contains the complete source code for building a **Custom LoRa to Wi-Fi Gateway**. 

Featured on the **IoTbhai** YouTube channel, this project bridges long-range, offline radio technology (LoRa) with modern web-based IoT dashboards. 

* **Node A (The Field Sensor):** Reads temperature and humidity from a DHT22, formats it into JSON, and transmits it miles away using the Reyax RYLR998.
* **Node B (The Gateway):** Receives the LoRa payload, extracts the Signal Strength (RSSI), and pushes the complete JSON data to an MQTT broker over Wi-Fi.
* **The Dashboard:** A beautiful, dark-mode/light-mode Material Design web dashboard built with Python, Flask, and WebSockets that updates in real-time without refreshing!

## 📺 Watch the Tutorial
*[Link to your YouTube Video will go here]*

## 🛠 Hardware Required
* **2x** ESP32 Development Boards (DOIT DevKit V1 or similar)
* **2x** Reyax RYLR998 LoRa Modules ([Product Link](https://reyax.com//products/RYLR998))
* **1x** DHT22 Temperature & Humidity Sensor
* **Jumper Wires** * **Power Source** (Power bank for Node A in the field)

## 🔌 Circuit Diagram & Wiring

To make things easy, **the RYLR998 wiring is exactly the same as our P2P tutorial!** You only need to add the DHT22 sensor to Node A. 

### Both Nodes (RYLR998 Wiring)
| RYLR998 Pin | ESP32 Pin | Function |
|-------------|-----------|----------|
| **VDD** | 3.3V      | Power    |
| **GND** | GND       | Ground   |
| **TX** | GPIO 16   | RX2      |
| **RX** | GPIO 17   | TX2      |

### Node A ONLY (DHT22 Wiring)
| DHT22 Pin | ESP32 Pin | Function |
|-----------|-----------|----------|
| **VCC** | 3.3V      | Power    |
| **GND** | GND       | Ground   |
| **DATA** | GPIO 4    | Sensor Data |

> **Note:** Ensure your antennas are firmly connected to the RYLR998 modules before powering them on to avoid damaging the RF chips.



### Wiring Schematic (Mermaid)
```mermaid
graph TD
    ESP32_A[Node A: ESP32]
    RYLR_A[RYLR998 Module]
    DHT[DHT22 Sensor]
    
    ESP32_A -- 3.3V --> RYLR_A(VDD)
    ESP32_A -- GND --> RYLR_A(GND)
    ESP32_A -- GPIO 17 (TX2) --> RYLR_A(RXD)
    ESP32_A -- GPIO 16 (RX2) --> RYLR_A(TXD)
    
    ESP32_A -- 3.3V --> DHT(VCC)
    ESP32_A -- GND --> DHT(GND)
    ESP32_A -- GPIO 4 --> DHT(DATA)
