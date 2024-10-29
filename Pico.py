from machine import UART, PWM, Pin, ADC
import time

# Initialize UART for serial communication
serial = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
serial.init(bits=8, parity=None, stop=1)

# Set up ADC for analog input
analog_input = ADC(Pin(26))

# Configure PWM output on a designated pin
pwm_output = PWM(Pin(0))
pwm_output.freq(1000)  # Set initial frequency to 1 kHz

# Initialize PWM duty cycle to 50% as a starting point
pwm_output.duty_u16(32768)  # 50% duty cycle

# Main loop for alternating send and receive operations
while True:
    # Part 1: Send duty cycle percentage
    # Read ADC value, update PWM, and send the value via UART
    analog_value = analog_input.read_u16()
    pwm_output.duty_u16(analog_value)  # Adjust duty cycle based on ADC reading

    # Convert the ADC value to a duty cycle percentage
    duty_cycle_percentage = int((analog_value / 65535) * 100)
    serial.write(f"{duty_cycle_percentage}\n")  # Send duty cycle as a string
    print(f"Sent duty cycle: {duty_cycle_percentage}%")

    # Short delay to give the other Pico time to receive
    time.sleep(0.5)  # Delay of 500 ms

    # Part 2: Receive duty cycle percentage
    # Check for incoming UART data
    if serial.any():
        incoming_data = serial.readline()
        if incoming_data:
            try:
                # Convert the received data back to an integer
                received_duty_cycle = int(incoming_data.strip())
                # Convert the percentage to a duty cycle value
                duty_cycle_value = int((received_duty_cycle / 100) * 65535)
                pwm_output.duty_u16(duty_cycle_value)  # Adjust PWM based on received value
                print(f"Received duty cycle: {received_duty_cycle}%")
            except ValueError:
                print("Invalid data received")

    # Delay before the next send-receive cycle
    time.sleep(0.5)
