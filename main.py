import socket

hostname= socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP:", ip)