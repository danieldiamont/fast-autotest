# Create a loopback serial port pair for demonstration purposes
socat -d -d pty,raw,echo=0 pty,raw,echo=0
