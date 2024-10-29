# UART, PWM, and ADC Control System

## Project Overview
This project demonstrates the use of UART communication, PWM signal control, and ADC input to create a basic microcontroller system for hardware control. The code is designed to adjust the PWM duty cycle based on ADC input, allowing for dynamic hardware control. Additionally, UART enables serial communication to monitor or adjust system parameters in real-time.

## Project Status
**Status**: Green  
The project is Completed and ready for demonstration.

## Work Plan and Milestones
Outlined below is our work plan, including major tasks and target completion dates:
- **Code Setup and Initialization** - Completed
- **UART and ADC Testing** - Completed
- **PWM Control Integration** - Completed
- **Final Testing and Adjustments** - Completed
- **Documentation and Submission** - Completed

This plan is being followed to ensure timely completion, and all tasks are meeting or are expected to meet their deadlines.

---

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup Instructions](#setup-instructions)
- [Code Structure and Functionality](#code-structure-and-functionality)
- [Usage](#usage)
- [Testing and Debugging](#testing-and-debugging)

---

## Features
- **UART Communication**: Enables serial data transmission and reception.
- **PWM Control**: Adjusts the PWM duty cycle based on ADC input.
- **ADC Integration**: Reads analog data and converts it to a digital value for PWM control.
- **Modular Code Design**: Ensures code clarity and ease of modification.

---

## Hardware Requirements
- Microcontroller (e.g., Raspberry Pi Pico)
- Circuit setup for UART and PWM functionality
- Jumper wires and breadboard

---

## Software Requirements
- MicroPython or CircuitPython installed on the microcontroller
- UART-compatible serial monitor software (e.g., PuTTY or Arduino Serial Monitor)

---

## Setup Instructions

### Hardware Setup
1. Configure the PWM output pin (default is Pin 0).
2. Connect UART TX and RX pins for serial communication (default is TX on Pin 8 and RX on Pin 9).

### Software Setup
1. Install MicroPython or CircuitPython on your microcontroller.
2. Clone this repository or copy the script directly to your microcontroller.
3. Ensure the serial monitor software is configured to match the UART settings (baud rate: 9600).

---

## Code Structure and Functionality

- **setup_uart(baud_rate=9600, tx_pin=8, rx_pin=9)**  
  Initializes UART communication with specified baud rate and TX/RX pins.

- **setup_adc(adc_pin=26)**  
  Configures ADC on the specified pin to read analog values.

- **setup_pwm(pwm_pin=0, frequency=1000, duty_cycle=32768)**  
  Sets up PWM on the specified pin, with a default frequency and duty cycle.

- **main_control_loop(uart, pwm, adc)**  
  Main loop to read ADC values and adjust PWM duty cycle. Also checks and processes incoming data on UART.

---

## Usage

### Run the Code
1. Upload the script to your microcontroller.
2. Open the serial monitor at the specified baud rate to observe UART communication.

### Functionality
- Real-time changes in PWM duty cycle can be observed on connected output devices.
- Use UART commands to adjust parameters dynamically if extended (custom commands can be added to the main loop).

### Notes
- Default frequency and duty cycle can be modified by changing parameters in `setup_pwm()`.

---

## Testing and Debugging
Our testing process includes:
- **UART Communication Testing**: Verifying data transmission and reception through the serial monitor.
- **ADC to PWM Mapping**: Ensuring accurate adjustment of PWM duty cycle based on ADC input values.
- **Error Checking**: Implementing UART data checks to handle any potential errors in incoming data.

Debugging logs and observations are documented in the project notes to support the final report and adjustments.

# References

We referenced code from The Raspberry Pi UART Documentation to assist with setting up and managing UART communication. Below are specific examples and their applications within this project.

### UART Initialization Example

- **Code Referenced**: `uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))`
- **How It Helped**: This setup example guided us in configuring UART communication, including specifying `baudrate`, `tx`, `rx`, `bits`, `parity`, and `stop` settings. It provided a foundation for establishing reliable serial communication between the Picos.

### Reading Data Over UART

- **Code Referenced**:
    ```python
    if uart.any():
        data = uart.read()
    ```
- **How It Helped**: This snippet demonstrated how to check for and read incoming UART data, ensuring that data was only read when available. We applied this to conditionally process incoming messages from the other Pico.

### Using `uart.any()` for Incoming Data

- **Code Referenced**: `if uart.any():`
- **How It Helped**: This function allowed us to implement a more efficient data flow check by verifying that data was ready before attempting to read, preventing errors from empty reads and ensuring the program only reads when necessary.

These references supported the setup of core UART functions. All application logic, including integrating ADC readings with PWM and managing data flow between devices, was independently developed for this project.
