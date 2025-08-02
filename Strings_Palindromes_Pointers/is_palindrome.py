# Time: O(log10n) -> removing digits
# Space: O(1) -> never creating new variables (constant extra space)
#- 
def efficient_is_palindrom(x):
    # cant be negative or multiple of 10 (unless its 0)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    def get_reversed_half_val(x, reversed_half):
        new_reveresed_half = reversed_half * 10
        new_reveresed_half += x % 10
        return new_reveresed_half
    
    def remove_final_digit(x):
        return x // 10

    reversed_half = 0    
    while x > reversed_half:
        reversed_half = get_reversed_half_val(x, reversed_half)
        x = remove_final_digit(x)
    
    return x == reversed_half or x == reversed_half // 10




# simple (O(n) + O(n))
def is_palindrome(x):
    if not x or x < 0 or x <= 2 or len(str(x)) % 2 == 0:
        return False
    
    str_num = str(x)
    mid_point_index = len(str_num) // 2
    print(mid_point_index)

    i, j = 0, len(str_num) - 1
    while i != mid_point_index and j != mid_point_index:
        if str_num[i] != str_num[j]:
            return False
        i += 1
        j -= 1

    return True




if __name__ == "__main__":
    is_palindrome(121)