import socket
import time
import serial

# Define the serial port
serial_port = serial.Serial('COM11', baudrate=9600, timeout=1)

def start_client():
    server_ip = '192.168.1.114'
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        data = client.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received from the server: {message}")
        l = message.split()[:4]
        print(l)
        message = str(l[1]) + " " + str(l[2]) + '\n'
        print("Send to Arduino",message)
        serial_port.write(message.encode('utf-8'))

        time.sleep(0.25)

    client.close()

start_client()