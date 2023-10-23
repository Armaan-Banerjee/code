import socket

with socket.socket() as s:
    s.bind(('localhost', 8231))
    s.listen(1)
    conn, addr = s.accept()

    while True:
        with conn:
            http_request = conn.recv(1024).decode('utf-8')
            request = parse_http(request)
            response = view(request)
            http_respnse = process_response(response)
            conn.sendall('hello world'.encode('utf-8'))


def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocl = request.split(' ')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )

    return method, path, protocl, headers, body

def process_response(response):
    return (
        'HTTP/1.1 200 OK\r\n'
        f'Content-Length: {len(response)}\r\n'
        'Content-Type: text/html\r\n'
        '\r\n'
        response
        '\r\n'
    )

def view(request):
    return request
