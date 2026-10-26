# Life-Beacon
ESP32-based elderly safety monitoring prototype with sensor monitoring, emergency alert logic, and dashboard.

## Problem Statement
Elderly people living alone may experience medical emergencies
without being able to call for help promptly.

## Proposed Solution
LifeBeacon is a prototype concept that uses sensor readings
to identify unusual patterns and demonstrate an alert workflow
for notifying trusted contacts.

## Hardware
- ESP32 microcontroller
- Heart-rate sensor
- Temperature sensor
- Movement sensor
- Sound sensor

## Workflow
Sensors -> ESP32 -> Data Processing -> Alert Logic
-> Dashboard -> Simulated SOS

## Software
- Python for demonstration alert logic
- ESP32 firmware planned in C/C++ or MicroPython
- Dashboard for sensor status and event logging

## Limitations
This is a prototype concept. Sensor integration, alert reliability,
and thresholds require testing and validation. It is not intended
for medical diagnosis or as a replacement for emergency services.
