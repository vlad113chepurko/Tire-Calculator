import socket
import json

PATH = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))
server.listen(1)

conn, addr = server.accept()
print(f'Conn from: {addr}')

while True:

    data = conn.recv(1024)

    if not data:
        print("Server closing...")
        break

    try:
        params = json.loads(data)
        width = int(params["width"])
        profile = int(params["profile"])
        diameter = int(params["diameter"])

        global_params = diameter * 25.4 + 2 * (width * (profile / 100))
        print(f"Res: {global_params}")
        response = json.dumps({"global_params": round(global_params, 2)})
        conn.send(response.encode())

    except Exception as e:
        print(f"Error: {e}")

conn.close()
server.close()