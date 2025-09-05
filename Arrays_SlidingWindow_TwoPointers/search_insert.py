# Time: O(log n) --> each iteration halves the the search range
# Space: O(1) --> fixed variables with no new data structures created therefore the input size doesnt matter
#-

def search_insert(nums, target):
    start_index = 0
    end_index = len(nums) - 1
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return start_index


if __name__ == "__main__":
    test = [-1,0,3,5,9,12]
    res = search_insert(test, 2)
    print(f"result: {res}")

    # [-1,0,3,5,9,12,14,15,17]