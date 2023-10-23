import socket

with socket.socket() as s:
    s.bind(('localhost', 8231))
    s.listen(1)
    conn, addr = s.accept()

    while True:
        with conn:
            request = conn.recv(1024).decode('utf-8')
            print(request)
            parse_http(request)
            conn.sendall('hello world'.encode('utf-8'))


def parse_http(request):
    *headers = request
