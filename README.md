# CS_361_Fun_Fact_Generator_Microservice

# Setting up your environment:
1. Download ZMQ

  Python example:
    
    pip install pyzmq

# Requesting data from the microservice:
1. Import ZMQ to your program
2. Set up a socket and connect to tcp://localhost:7424
3. Send a __string__ to the server containing the requested topic for the fun fact

   Python example:

```
     import zmq
   
     context = zmq.Context()
     socket = context.socket(zmq.REQ)
     socket.connect("tcp://localhost:7424")

     topic = "history"
     socket.send_string(topic)
```

# Receiving data from the microservice:
1. Follow the instructions in [Requesting data from the microservice](#requesting-data-from-the-microservice)
2. Call socket.recv() to receive the microservice's response. This will be a string.
3. Make sure to call .decode() on the recv'd data. Then, you can use the data as an ordinary string.

   Python example:

   ```
      import zmq

       # code to request data --- see above

       response = socket.recv()
       decoded = response.decode()  # decoded now holds a string!
    
   ```
   
# UML Sequence:
img goes here
