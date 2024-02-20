Steps:

1. Accept route update messages from the BGP neighbors, and forward updates as appropriate

2. Accept route revocation messages from the BGP neighbors, and forward revocations as appropriate

3. Forward data packets towards their correct destination
Return error messages in cases where a data packet cannot be delivered

4. Coalesce forwarding table entries for networks that are adjacent and on the same port

5. Serialize your routing table cache so that it can be checked for correctness

6. Your program must be called 3700router



 For the sake of simplicity, all of the neighboring routers will have IP addresses of the form ...2 and all of the IP addresses used by router router will be of the form ...1.

