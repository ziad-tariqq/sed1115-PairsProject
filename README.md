# UART, PWM, and ADC Control System

## Project Overview
This project demonstrates the use of UART communication, PWM signal control, and ADC input to create a basic microcontroller system for hardware control. The code is designed to adjust the PWM duty cycle based on ADC input, allowing for dynamic hardware control. Additionally, UART enables serial communication to monitor or adjust system parameters in real-time.

## Acknowledgment
This project was inspired by publicly available project structures, with modifications for enhanced functionality, readability, and modularity. Developed as part of an educational initiative, all reused components are credited appropriately, and no licenses are violated.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup Instructions](#setup-instructions)
- [Code Structure and Functionality](#code-structure-and-functionality)
- [Usage](#usage)

## Features
- **UART Communication**: Enables serial data transmission and reception.
- **PWM Control**: Adjusts the PWM duty cycle based on ADC input.
- **ADC Integration**: Reads analog data and converts it to a digital value for PWM control.
- **Modular Code Design**: Ensures code clarity and ease of modification.

## Hardware Requirements
- Microcontroller (e.g., Raspberry Pi Pico)
- Circuit setup for UART and PWM functionality
- Jumper wires and breadboard

## Software Requirements
- MicroPython or CircuitPython installed on the microcontroller
- UART-compatible serial monitor software (e.g., PuTTY or Arduino Serial Monitor)

## Setup Instructions

### Hardware Setup
1. Configure the PWM output pin (default is Pin 0).
2. Connect UART TX and RX pins for serial communication (default is TX on Pin 8 and RX on Pin 9).

### Software Setup
1. Install MicroPython or CircuitPython on your microcontroller.
2. Clone this repository or copy the script directly to your microcontroller.
3. Ensure the serial monitor software is configured to match the UART settings (baud rate: 9600).

## Code Structure and Functionality

- `setup_uart(baud_rate=9600, tx_pin=8, rx_pin=9)`  
  Initializes UART communication with specified baud rate and TX/RX pins.

- `setup_adc(adc_pin=26)`  
  Configures ADC on the specified pin to read analog values.

- `setup_pwm(pwm_pin=0, frequency=1000, duty_cycle=32768)`  
  Sets up PWM on the specified pin, with a default frequency and duty cycle.

- `main_control_loop(uart, pwm, adc)`  
  Main loop to read ADC values and adjust PWM duty cycle. Also checks and processes incoming data on UART.

## Usage

### Run the Code
1. Upload the script to your microcontroller.
2. Open the serial monitor at the specified baud rate to observe UART communication.

### Functionality
- Real-time changes in PWM duty cycle can be observed on connected output devices.
- Use UART commands to adjust parameters dynamically if extended (custom commands can be added to the main loop).

### Notes
- Default frequency and duty cycle can be modified by changing parameters in `setup_pwm()`.
