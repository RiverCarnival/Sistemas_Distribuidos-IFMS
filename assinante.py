import zmq


context = zmq.Context()
sock = context.socket(zmq.SUB)

sock.connect("tcp://localhost:5556")

topic = "Teste"

sock.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
    menssagem = sock.recv_string()
    print(menssagem)