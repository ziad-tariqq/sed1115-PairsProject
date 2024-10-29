from machine import UART, PWM, Pin, ADC
import time

# Configure the device mode: set to 'send' on one Pico and 'receive' on the other
mode = 'send'  # Change to 'receive' for the other device

# Initialize UART for serial communication
serial = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
serial.init(bits=8, parity=None, stop=1)

# Set up ADC for analog input (only used by the sender)
analog_input = ADC(Pin(26))

# Configure PWM output on a designated pin
pwm_output = PWM(Pin(0))
pwm_output.freq(1000)  # Set initial frequency to 1 kHz

# Main loop for send and receive operations
while True:
    if mode == 'send':
        # Read ADC value, update PWM, and send the value via UART
        analog_value = analog_input.read_u16()
        pwm_output.duty_u16(analog_value)  # Adjust duty cycle based on ADC reading

        # Send the analog value as a duty cycle percentage over UART
        duty_cycle_percentage = int((analog_value / 65535) * 100)
        serial.write(f"{duty_cycle_percentage}\n")  # Send duty cycle as a string
        print(f"Sent duty cycle: {duty_cycle_percentage}%")

        # Delay to avoid flooding the receiver
        time.sleep(0.5)  # Delay of 500 ms

    elif mode == 'receive':
        # Check for incoming UART data
        if serial.any():
            # Read the received data and convert it to an integer
            incoming_data = serial.readline()
            if incoming_data:
                try:
                    received_duty_cycle = int(incoming_data.strip())
                    # Convert percentage back to duty cycle value for PWM
                    duty_cycle_value = int((received_duty_cycle / 100) * 65535)
                    pwm_output.duty_u16(duty_cycle_value)  # Adjust PWM based on received value
                    print(f"Received duty cycle: {received_duty_cycle}%")  # Print received value
                except ValueError:
                    print("Invalid data received")

        # Delay for stability
        time.sleep(0.2)  # Delay of 200 ms
