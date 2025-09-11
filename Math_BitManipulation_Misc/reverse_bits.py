# Time: O(1) 
# Space: O(1)
#-

def reverse_bits(n):
    n &= 0xFFFFFFFF
    res = 0
    for _ in range(32):
        # extract last bit and append to front
        res = (res << 1) | (n & 1) 
        n >>= 1 # shift everything right once 
    return res

if __name__ == "__main__":
    reverse_bits(43261596)