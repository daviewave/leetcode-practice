# Time: O(log x) -> use binary search since after the initial check to ensure x is larger than 1 that the sqrt must be at least 2 but will not ever be more than x / 2 (4) so those can be used as the starting and ending indexs and traverse based on that
# Space: O(1) no new structures created
#-

def sqrt_x_binary(x):
    if x < 2:
        return x
    
    start, end = 2, x // 2
    while start <= end:
        mid = (start + end) // 2
        sqrt = mid * mid

        if sqrt == x:
            return mid
        elif sqrt < x:
            start = mid + 1
        else:
            end = mid - 1
    return end

# Time: O(log x) -> although its the same as the binary search method, it converges much quicker on larger x values -- confused me at first but when looking closer the PEMDAS rules ensure that the first operation done in the while loop is 'x // guess' so it does work with 8 for example
# Space: O(1) no new structures created
#-

def sqrt_x_newtons(x):
    if x < 2:
        return x
    
    guess = x // 2
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    return guess 

if __name__ == "__main__":
    # sqrt_x_binary(8)
    sqrt_x_newtons(8)