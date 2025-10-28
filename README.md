# IoTprojekt
# 🚗 Azure IoT Vehicle Tracking System

A Vehicle Tracking System designed to simulate, process, and visualize real-time vehicle location and telemetry data.  
This project demonstrates how IoT, data analytics, and cloud visualization can be integrated to build a scalable, intelligent tracking system.

# 🧭 Overview

This project tracks and visualizes the real-time location and speed of multiple vehicles using simulated IoT devices that send data to Azure IoT Hub.  
The data is then processed via Azure Stream Analytics stored in Azure Cosmos DB and visualized on a Power BI dashboard and Azure Maps interface.

# 🏗️ Architecture

```text
┌──────────────────────────┐
│  Simulated Vehicle Device│
│  (Azure IoT Simulator)   │
│  • Sends GPS + speed data│
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Azure IoT Hub       │
│  • Receives telemetry    │
│  • Manages devices       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Azure Stream Analytics  │
│  •Real-time processing   │
│  •Filtering & aggregation│
│  •Routing to outputs     │
└─────────┬──────┬─────────┘
          │      │
          ▼      ▼
┌────────────────────────┐     ┌──────────────────────┐
│  Azure Cosmos DB       │     │  Azure Logic Apps /  │
│  • Stores route history│     │  Event Grid (Alerts) │
└─────────┬──────────────┘     └─────────────┬────────┘
          │                                  │
          ▼                                  │
┌──────────────────────────┐                 │
│       Azure Maps         │◄────────────────┘
│  • Live map visualization│
│  • Route playback        │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│     Power BI Dashboard   │
│  • Vehicle analytics     │
│  • Speed, route, alerts  │
└──────────────────────────┘
