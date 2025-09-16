# Time: O(log n)
# Space: O(1)
#-
# is assuming an API method called 'isBadVersion' exists


def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
        return left

if __name__ == "__main__":
    first_bad_version()