# Time: O(n) -> depends on the size of the input list
# Space: O(1) -> no new data structures created, only use a int variable
#-
# when using the XOR bitwise manipulation starting with 0, duplicate values will cancel each other out and after every item in the array is executed, the bitwise value will be the only single value 

def single_number_xor(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res


# Time: O(n) -> faster than the XOR method because it returns as soon as it finds the value that = 1
# Space: O(1) -> no new data structures created, only use a int variable
#-
# use pythons built in Counter data structure

from collections import Counter
def single_number_counter(nums):
    counter = Counter(nums)
    for num, total in counter.items():
        if total == 1:
            return num

if __name__ == "__main__":
    single_number_xor([4, 2, 1, 2, 1])