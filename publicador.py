import zmq

text = zmq.Context()

sock = text.socket(zmq.PUB)

sock.bind("tcp://*:5556")

while True:
    
    print("Insira o que deseja enviar")
    
    topic = "Teste"
    #mensagem = input()
    sock.send_string(topic)

