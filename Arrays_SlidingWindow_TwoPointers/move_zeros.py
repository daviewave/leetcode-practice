# Time: O(n) -> depends on the size of the nums array passed in 
# Space: O(1) -> no extra space needed
#-
# similar to the remove duplicates want a slow and fast pointer where the slow tracks the
# index of the next place to insert an results that meet the conditions the fast pointer finds 

def move_zeros(nums):
    if nums and len(nums) > 1:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1       

if __name__ == "__main__":
    move_zeros()