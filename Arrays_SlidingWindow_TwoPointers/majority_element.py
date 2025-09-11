# Time: O(n) -> 1 pass through 
# Space: O(n) -> counter object created
#-


def majority_element(nums):
    from collections import Counter
    counter = Counter(nums)
    
    for val, total in counter.items():
        if total >= len(nums) / 2:
            return val

if __name__ == "__main__":
    majority_element()