# Time: O(n)
# Space: O(n)
#-
# first ensure that both strings are equal lengths by padding the smaller with leading 0's, then reverse loop through to perform the addition of each bit using the carry to inject an extra '10' when the sum is = 2 
 

def add_binaries(a: str, b: str):
    leader = max(len(a), len(b))
    a = a.zfill(leader)
    b = b.zfill(leader)
    
    result = []
    carry = 0
    for i in range(leader - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        result.append(str(digit_sum % 2))
        carry = digit_sum // 2
    
    if carry:
        result.append("1")
    
    return ''.join(reversed(result))

if __name__ == "__main__":
    add_binaries()