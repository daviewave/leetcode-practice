# Time: O(n)
# Space: O(n)
#-


def summary_ranges(nums):
    if len(nums) == 1:
        return [f"{nums[0]}"]
    
    res = []
    i = 0
    for index, num in enumerate(nums):          
        if abs(num - nums[index - 1]) > 1:
            if index - i > 1:
                res.append(f"{nums[i]}->{nums[index - 1]}")
                i = index
            
            if num == nums[-1]:
                res.append(f"{num}")
                i = index
            
            elif abs(nums[index + 1] - num) > 1:
                res.append(f"{num}")
                i = index + 1
        elif num == nums[-1]:
            res.append(f"{nums[i]}->{num}")
    return res   

if __name__ == "__main__":
    summary_ranges([0, 2, 3, 4, 6, 8, 9])