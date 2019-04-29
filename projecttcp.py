import socket
import sys
import base64
import subprocess
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', int(sys.argv[1]))
print ('starting up on %s port %s'% server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print ('connection from', client_address)
    #data = ""
    # Receive the data in small chunks and retransmit it
    fulldata = []
    end=b'NNNNN'
    while True:
        data = connection.recv(40960000)
        if end in data:
            fulldata.append(data[:data.find(end)])
            break
        fulldata.append(data)
        if len(fulldata)>1:
            #check if end_of_data was split
            last_pair=fulldata[-2]+fulldata[-1]
            if end in last_pair:
                fulldata[-2]=last_pair[:last_pair.find(end)]
                fulldata.pop()
                break
    newdata = b''.join(fulldata)
    image = base64.decodebytes(newdata + b'===')
    f = open('data/actual/environment/run.jpg','wb')
    f.write(image)
    f.close()
    subprocess.run(args=['python','Comp-Vis-Tour.py'])
    f = open('landmark.html', 'r')
    retdata = f.read()
    f.close()
    print ('sending data back to the client')
    connection.sendall(retdata.encode())
    connection.close()

