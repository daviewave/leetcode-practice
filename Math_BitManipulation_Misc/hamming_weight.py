# Time: O(k) or O(log n) -> relative to normal and in terms of bits
# Space: O(1) 
#-

def hamming_weight(n):
    return bin(n).count("1")

if __name__ == "__main__":
    hamming_weight(11)