"""
UDP Ping Server
Talib Pierson
Fri Feb 12
"""
import random
import socket as s

# SOCK_DGRAM for UDP
SOCK = s.socket(s.AF_INET, s.SOCK_DGRAM)
# Assign IP address and port number to socket
SOCK.bind(('', 12000))

while True:
    # Receive client packet and arrival address
    msg, host = SOCK.recvfrom(1024)
    # Capitalize the message
    msg = msg.upper()

    # Error simulator; send response with 75% success rate
    if random.random() < 0.75:
        SOCK.sendto(msg, host)
