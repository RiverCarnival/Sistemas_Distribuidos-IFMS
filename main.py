import asyncio
import socket
import threading

def client():
    IP_Servidor = '10.8.38.107'             

    PORTA_Servidor = 8080

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("Digite seu nome:")
    # name = input()

    DESTINO = (IP_Servidor, PORTA_Servidor) 
    try:
        tcp.connect(DESTINO) 
        while 1:
            print("Digite a mensagem:")
            message = input()   
            
            tcp.send(bytes(message,"utf8"))
            if(message == "q"):
                break
        tcp.close()
    except:
        tcp.close()

async def server():
    HOST = '10.8.38.107'              
    PORT = 8080

    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (HOST, PORT)
        tcp.bind(orig)
        tcp.listen(1)

        while True:
            con, cliente = tcp.accept()
            print('Conectado por', cliente)
            while True:
                msg = con.recv(1024)
                if msg == 'q': break 
                print( msg)
            con.close()
        tcp.close()

    except: 
        tcp.close()

loop = asyncio.get_event_loop()

def aaaaa():
    loop.create_task(server())
    loop.run_until_complete(server())


threadServer = threading.Thread(target=aaaaa,args=())
threadClient = threading.Thread(target=client, args=())
verif = False
# while True:
threadServer.start()
threadClient.start()

    


