import socket


def handle_request(conn):
    buf = conn.recv(1024)
    conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
    conn.send('<h1 style=\'color:red\'>hhhhh<h1/>'.encode('utf-8'))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()