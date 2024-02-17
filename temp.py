# ----------- Helpers ---------------


# Returns binary string of length 32 with
# specific 1s from left and remaining bits are 0s
def get_binary_mask(mask):
    # We assume IPv4 address

    return ('1' * mask) + ('0' * (32 - mask))
    
# Takes IP String and returns 32 bit Binary
def ip_to_binary(ip: str):
    
    ip_vals = ip.split('.')
    ip_bin = [bin(int(x))[2:].zfill(8) for x in ip_vals]
    
    return ''.join(ip_bin)

# Takes 2 binary strings and performs
# and operation and returns result.
def and_bin_str(bin1, bin2):
    
    if len(bin1) != len(bin2):
        return -1 # error
    
    i = 0
    res = list(bin1)
    while i < len(bin2):
        if bin2[i] == '0':
            res[i] = '0'
        
        i += 1
    
    return ''.join(res)

# Takes an ip address and returns consecutive ones
# from left till 0 is detected
def count_consecutive_ones(ip_address):
    
    ip_binary = ip_to_binary(ip_address)
    ones = 0
    
    for bit in ip_binary:
        if bit == '0':
            break
        ones += 1
    
    return ones

# gets 2 ip addresses
# applies mask on both and compares result
# if same then within network
def is_within_network(ip, network, mask):
    
    mask_bin = get_binary_mask(mask)
    ip_binary1 = ip_to_binary(ip)
    ip_binary2 = ip_to_binary(network)
    
    return and_bin_str(ip_binary1, mask_bin) == and_bin_str(ip_binary2, mask_bin)

def prefix_match(ip, network, mask):
    
    bin_mask    = get_binary_mask(mask)
    bin_network = ip_to_binary(network)
    bin_ip      = ip_to_binary(ip)
    
    res = and_bin_str(bin_network, bin_mask)
    
    prefix_match = 0
    for d1, d2 in zip(res, bin_ip):
        if d1 == d2:
            prefix_match += 1
    
    return prefix_match

# ---------- Helpers ----------------

f_table = {'192.168.0.2': [('12.0.0.0', 8)], 
 '172.168.0.2': [('172.169.0.0', 16), ('172.0.0.0', 8)], 
 '10.0.0.2': [('12.0.0.0', 8)]}


# Situations where we need to adjust this table!

# Scenario 1: Router has one possible route to the destination network
# Scenario 1: Multiple Routes possible.


# How to deal with this?
# So, first I can make a list of routes that are possible
# then, I will pass that list of routes to below function
# below function will return me the most optimal route










# Helper function to get prefix match

print(prefix_match('172.128.88.99', '172.0.0.0', 8))
print(prefix_match('172.128.88.99', '172.128.0.0', 9))

# So, we choose 
# result1 = and_bin_str(bin_network, bin_mask)

# (Done) Case 1: 2 possible routes
#               Pick 1 with the longest prefix match 

# Case 2: multiple routes
#
def get_optimal_route(ip, routes):
    
    
    # Case 1: Longest Prefix M
    if len(routes) == 2:
        # Return route with longest prefix
        # maybe netmask1 > netmask2: then, we are good to go with network 1
        network1, mask1 = routes[0]
        network2, mask2 = routes[1]
        
        if prefix_match(ip, network1, mask1) > prefix_match(ip, network2, mask2):
            return (network1, mask1)
        else:
            return (network2, mask2)
        

print(get_optimal_route('172.128.88.99', [('172.0.0.0', 8), ('172.128.0.0', 9)]))