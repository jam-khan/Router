# Router

This project was made as part of coursework for CS3700 at Northeastern University.

# High-Level Approach:

Updating:
Upon receiving an update message, the router processes the message, updates its forwarding table, and broadcasts the updated information to its neighbors.

Withdrawing:
When receiving a withdraw message, the router removes the corresponding route from its forwarding table and broadcasts the withdrawal to its neighbors. 

Dumping:
If requested to dump its forwarding table, the router sends its current forwarding table to the specified destination.

Sending Data:
After receiving a data message from an IP address, the router determines the best route for the destination and forwards the message. If no route is found, it responds with a "no route" message.

Aggregation:
The router aggregates routes in its forwarding table to reduce the number of entries, optimizing routing efficiency. It does this by checking if routes have the same attributes and if they are numerically adjacent (then they can be grouped together as part of a larger network)

Disaggregation:
After withdrawing a route, the router disaggregates its forwarding table when it sees neccessary to maintain accurate routing information. This involves restoring previously aggregated routes to their original entries if the withdrawn route affects validity.

Helper Functions we used:
IP to Binary Conversion: Converts an IP address to its binary representation.
Binary to IP Conversion: Converts a binary string back to its IP address format.
Binary Operations: Performs bitwise operations like AND on binary strings.
Count Consecutive Ones: Determines the number of consecutive ones in a binary string, useful for calculating subnet masks.
Is Within Network: Checks if an IP address falls within a given network and mask.
Get IP Value: Calculates a numerical value for an IP address, used for sorting routes.
Get Binary Mask: Generates a binary subnet mask based on the mask length.

# Challenges Faced:

Route Aggregation: Designing and implementing the logic for aggregating routes efficiently was a significant challenge for us, because it required some time to understand the intended requirement and a careful consideration of route attributes and prefix matching. 

Complex Functionality: Functions like find_route and handle_update involved complex logic and decision-making based on various route attributes, leading to intricate code structures.

Optimization: Ensuring the efficiency and performance of the routing algorithms and data structures gave us many challenges, particularly in the situations where there were large routing tables or frequent updates.

Features/Properties of the Design:

We have kept it modular as much as possible hence we have an extensive range of helper languages. We have cleaned the code as much as we can to avoid redudancy, promoting maintainability and scalability.

Other features that we think are interesting:

Dynamic Routing: The router dynamically updates its forwarding table based on received messages, enabling adaptive routing behavior.
Efficient Routing: Utilizes route aggregation and optimized route selection algorithms to improve routing efficiency and reduce overhead.

We tested our code frequently with the given test config files and printing various statements throughout the code for debugging.
