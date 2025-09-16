# Time: O(n) -> larger numbers passed in will be divided more times than smaller numbers so it depends on the size of n
# Space: O(1)
#-


def is_ugly(n):
    if n <= 0:
        return False

    for pf in [2, 3, 5]:
        while n % pf == 0:
            n //= pf
    return n == 1

if __name__ == "__main__":
    is_ugly(14)