# Time: O(n)
# Space: O(n)
#-

def reverse_integer(x):
    def is_32bit_signed(new):
        return -2**31 <= new <= 2**31 - 1
        
    if x < 0:
        x = list(str(x)[1:])
        x.reverse()
        x.insert(0, '-')
    else:
        x = list(str(x))
        x.reverse()
    x = int(''.join(x))
    
    if not is_32bit_signed(x):
        return 0
    return x

if __name__ == "__main__":
    reverse_integer(-321)