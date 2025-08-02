# Time: O(n) -> list traversed one time
# Space: O(n) -> created dict for storage
#-
# instead of directly comparing index values, for each index's value determine
# what number would satisfy the target and if its not in dict of values seen
# add it, if it is we know that those 2 indexs equal the target and return that

def two_sum(nums, target):
    compliment_lookup = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in compliment_lookup:
            return [compliment_lookup[compliment], i]
        compliment_lookup[num] = i


if __name__ == "__main__":
    two_sum([3, 5, 6, 2], 8)