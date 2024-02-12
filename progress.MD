Implementing a simple BGP router

BGP router will run inside a simulator

It has to accomplish all essential features of an actual router:

1. Accepting route announcements from simulated peer routers.
2. Generating a new route announcements for your peer routers
3. Managing and Compressing a forwarding table
4. Forwarding data packets that arrive from simulated internet users.

<!-- Testing -->
1. Correctness
    1. Correct Routing Announcements
    2. Forwarding Data Packets to correct destination
2. Performance
    1. Generating Compressed forwarding table by aggregating forwarding entries when possible.

- Need to pass 16 test cases to assess functionality.

<!-- Illegal Libraries -->
1. All code for IP address manipulation must be written by student. DON'T USE ipaddress module.





<!-- Connecting to Neighbours -->

 However, rather than sending and receiving packets over the internet, the packets are instead passed between programs on the local machine. In other words, this is how your program will send and receive data from our simulator, which is just another program running locally on the machine. For example, to send to a message to a specific neighbor, send the message in packet using a UDP socket to the UDP port the neighbor is listening on. You should constantly be reading from your sockets to make sure you receive all messages (they will be buffered if you don’t read immediately). 

 <!-- Handling Multiple Sockets -->
 We encourage you to write your code in an event-driven style using select() or poll() on all of the domain sockets that your router is connected to (see the starter code for an example). This will keep your code single-threaded and will make debugging your code significantly easier. Alternatively, you can implement your router in a threaded model (with one thread handling each socket), but expect it to be significantly more difficult to debug.

 <!-- Message Format -->
 Using JSON for message format.
 {
  "src":  "<source IP>",
  "dst":  "<destination IP>",
  "type": "<update|withdraw|data|no route|dump|table|handshake>",                   
  "msg":  {...}
}
-   Message Types
1. update:
    Route annoucements! When router receives route announcement from a neighbour.
    Step 1: Save a copy of the announcement for later use.
    Step 2: Add an entry to your forwarding table.
    Step 3: Potentially send copies of annoucements to neighbouring routers.

    Form:
    {
        "src":  "<source IP>",        # Example: 172.65.0.2
        "dst":  "<destination IP>",   # Example: 172.65.0.1  Notice the final one, this will typically be the IP address of your router
        "type": "update",                   
        "msg": 
        {
            "network":    "<network prefix>",           # Example: 12.0.0.0
            "netmask":    "<associated subnet netmask>",# Example: 255.0.0.0
            "localpref":  "<integer>",                  # Example: 100
            "selfOrigin": "<true|false>",
            "ASPath":     "{<nid>, [nid], ...}",        # Examples: [1] or [3, 4] or [1, 4, 3]
            "origin":     "<IGP|EGP|UNK>",                    
        }
    }

    Using the example above as a guide, this route announcement is telling your router that your neighbor (172.65.0.2) knows how to forward data packets to the 12.0.0.0/8 network. In the future, if your router were to receive a data packet whose destination IP was in this network (e.g., 12.4.66.13), then your router should forward the data packet to this neighbor.

    "network" and "netmask": fields describe network that is routable.
    "localpref": "weight" assigned to this route, where HIGHER weights are better.
    "selfOrigin" (true or false): true is preferred. Tells if route was added by local administrator (true) or not (false).
    "ASPath": list of Autonomous Systems (ASs) that the packet along this route will traverse. Preference is given to routes with shorter ASPath
    “origin” describes whether this route originated from a router within the local AS (IGP), a remote AS (EGP), or an unknown origin (UNK), where the preference order is IGP > EGP > UNK. 

2. withdraw
3. data
4. no route
5. dump
6. table

7. handshake:

    When your router starts up, it needs to send a “handshake” message to each of your neighboring routers to let the neighbor know it is up. 