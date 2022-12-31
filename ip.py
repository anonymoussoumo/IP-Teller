import pyfiglet
import socket

def gather_ip_address():
    # Get the hostname of the machine
    hostname = socket.gethostname()
    # Get the IP address of the machine
    ip_address = socket.gethostbyname(hostname)

    return ip_address

# Display a message in ASCII art
ascii_text = pyfiglet.figlet_format("IP Teller", font="slant")
print (ascii_text)

# Gather and display the IP adress
ip_address = gather_ip_address()
print("Your IP Address Is:", ip_address)
