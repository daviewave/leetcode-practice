# Time: O(m + n) -> depends on the size of both array1 and array2 passed in
# Space: O(1) -> no new structures created just altering the array1
#- 

def merge_sorted_arrays(nums1, nums2):
    i, j = m - 1, n - 1
    k = len(nums1) - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

if __name__ == "__main__":
    merge_sorted_arrays()