import json
import zmq

def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7424")

    topic = "animals"

    socket.send_string(topic)

    response = socket.recv()

    decoded = response.decode()
    
    print("Fun fact:", decoded)

    context.destroy()


if __name__ == "__main__":
    client()