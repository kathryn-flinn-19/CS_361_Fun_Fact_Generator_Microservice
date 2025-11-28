# for fun fact generator
import zmq
import random

"""
have a pool of fun fact objects
ex object: {"topic": "txt", "fact": "txt"}

then, if the requested topic matches the topic of the fun fact, add 
it to a list and then choose a random one

same format as image retrieval microservice
"""

facts = [{"topic": "animals", "fact": "A group of rats is called a mischief"}, 
         {"topic": "animals", "fact": "Ants do not have lungs --- they breathe through holes called spiracles"},
         {"topic": "animals", "fact": "The fat-tailed lemur is the only animal that dreams during hibernation"},
         {"topic": "science", "fact": "There are more stars in the universe than grains of sand on Earth"},
         {"topic": "science", "fact": "A lightning bolt is 30,000 degrees Celsius --- five times hotter than the surface of the Sun"},
         {"topic": "science", "fact": "You can yo-yo in space"},
         {"topic": "nature", "fact": "Fungi is more closely related to animals than plants"},
         {"topic": "nature", "fact": "There are more trees on Earth than there are stars in the Milky Way"},
         {"topic": "nature", "fact": "Asparagus is a member of the Lily family"},
         {"topic": "history", "fact": "Napolean Bonaparte was once attacked by a swarm of rabbits"},
         {"topic": "history", "fact": "USPS once allowed customers to send children through the mail"},
         {"topic": "history", "fact": "Australia declared war on emus in 1932"}]

def topic_in_pool(topic):

    for f in facts:
        if topic == f["topic"]:
            return True

    return False

def choose_fact(topic):
    pool = []

    for f in facts:
        if topic == "random":
            pool.append(f["fact"])
        elif topic == f["topic"]:
            pool.append(f["fact"])
    
    return random.choice(pool)

def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)

    socket.bind("tcp://*:7424")

    while True:
        # receive and decode a request from the client

        message = socket.recv()

        full_msg = message.decode()

        # if asked to quit, break
        if full_msg == "Q":
            break

        topic = ""

        if not topic_in_pool(full_msg):
            topic = "random"
        else:
            topic = full_msg

        response = choose_fact(topic)

        socket.send_string(response)

    context.destroy()
    socket.close()

if __name__ == "__main__":
    server()

"""
data visualization society early career committee
nasa scientific visualization studio
weather layers
mapboxgl js
omsi planetarium
openusd 
"""