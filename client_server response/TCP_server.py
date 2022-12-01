import socket


server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host=192.168.189.2
host=socket.gethostname()
port=444

server_socket.bind(('192.168.189.2', port)) # host will be replaced/subtituted with ip, if changed and not running on host.

#starting TCP listner
server_socket.listen(3)

while True:
    #starting tcp connection
    client_socket,address = server_socket.accept()

    print('recieved connection from %s' % str(address))

    message='thank you! for connecting our server.this is an example of how sock ' + "\r\n"
    client_socket.send(message.encode('ascii'))

    client_socket.close()
  