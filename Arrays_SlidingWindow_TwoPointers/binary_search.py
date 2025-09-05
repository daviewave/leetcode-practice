# Time: O(log n) --> each iteration halves the the search range
# Space: O(1) --> fixed variables with no new data structures created therefore the input size doesnt matter
#-

def binary_search(nums, target):
    if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
        return -1

    start_index = 0
    end_index = len(nums) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return -1


if __name__ == "__main__":
    test = [-1,0,3,5,9,12]
    res = binary_search(test, 2)
    print(f"result: {res}")

    # [-1,0,3,5,9,12,14,15,17]