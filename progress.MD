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

