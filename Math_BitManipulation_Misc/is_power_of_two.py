# Time: O(n)
# Space: O(1)
#-

def is_power_of_two(n):
    if n < 1:
        return False
        
    if n == 1 or n == 2:
        return True
    
    remainder = 0
    while True:
        remainder = n % 2
        if remainder != 0:
            return False
        if n == 2:
            return True
        n = n / 2

if __name__ == "__main__":
    is_power_of_two(64)