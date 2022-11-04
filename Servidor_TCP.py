# Feito por Valdemir Chaves Ribeiro
import socket

HOST = '10.8.34.123'              
PORT = 8080

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    while True:
        
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)
    print('Finalizando conexao do cliente', cliente)
    con.close()