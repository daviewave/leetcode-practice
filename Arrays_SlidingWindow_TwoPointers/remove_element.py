#- mine
# Time: O(n) -> if only 1 .pop is needed but O(n^2) if multiple 
# Space: O(1) -> not creating new list just altering
#- best
# Time: O(n) -> since only going through nums once
# Space: O(1) -> not creating new list
# 

def remove_element_mine(nums, val):
        if len(nums) == 0:
            return 0
        
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            i -= 1
        return len(nums)


def remove_element_best(nums, val):
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    remove_element_mine()