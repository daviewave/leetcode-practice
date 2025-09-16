# Time: 
# Space:
#-


def missing_number_mine(nums):
    from collections import Counter
    counter = Counter(nums)
    i = 0
    while i <= len(nums):
        if not counter[i]:
            return i
        i += 1
    return i

# works in python since python protects against integer overflow
def missing_number_best_python(nums):
    sum_arr = sum(nums)
    return (len(nums) * (len(nums) + 1)) // 2 - sum_arr


# in languages like C/C++/Java need to prevent int overflow so XOR bitwise method is best approach 
def missing_number_xor(nums):
    n = len(nums)
    res = n
    for i, num in enumerate(nums):
        res ^= i ^ num
    return res

if __name__ == "__main__":
    missing_number_mine([3, 0, 1, 4, 6, 5])