# Time: O(n) -> depends on size of list passed in
# Space: O(1) -> no new data structures created
#-
# use the 2 pointer method where the one outside of the loop is the slow and inside is the fast
# and since its an ordered list, we know if we find a new one that is the only time it will show
# up so we move the slow index up and set its value to the current value of j's index if the have
# different values at the current index's in the loop

def remove_duplicates(nums):
    if not nums or len(nums) == 0:
        return 0
    
    slow_index = 0
    for fast_index in range(1, len(nums)):
        if nums[slow_index] != nums[fast_index]:
            slow_index += 1
            nums[slow_index] = nums[fast_index]
    nums[:] = nums[:slow_index+1] # to truncate the list to only the remaining
    return slow_index + 1


if __name__ == "__main__":
    remove_duplicates([1, 1, 2, 3, 7, 8, 8, 11, 12, 14, 15, 15])