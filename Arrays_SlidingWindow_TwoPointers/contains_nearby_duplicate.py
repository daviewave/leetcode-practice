# Time: 
# Space:
#-
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k

def contains_nearby_duplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False

if __name__ == "__main__":
    contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)