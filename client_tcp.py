#Feito por Gabiel Patrocinio
import socket

IP_Servidor = '10.8.34.125'             

PORTA_Servidor = 8080

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Digite seu nome:")
name = input()

DESTINO = (IP_Servidor, PORTA_Servidor) 

tcp.connect(DESTINO) 
while 1:
 message = input()   
 message = name + ": " + message
 
 tcp.send(bytes(message,"utf8"))
 if(message == name+": q"):
     break
  
tcp.close()
