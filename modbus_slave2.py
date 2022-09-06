import socket

# запускаем slave-устройство (конвертер)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 6453

hostname = socket.gethostname()
s.bind((hostname, PORT))
print('Listening for broadcast at ', s.getsockname())

while True:
    data, address = s.recvfrom(1024)
