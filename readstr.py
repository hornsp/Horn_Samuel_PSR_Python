def read_string(sock):
    received_data = b""
    while True:
        chunk = sock.recv(1)
        if not chunk or chunk == b'\n':
            break
        received_data += chunk
    return received_data.decode()