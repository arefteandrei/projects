import socket
import time

server_port = 21060

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()
input_s = 'Hello, server!2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222'
client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)
print('[CLIENT] Response from server {}, is: "{}"'.format(address, str(input_s_modified.decode('utf8'))))
end = time.time()
print("The time for sending message is: ", end - start)

client_socket.close()
