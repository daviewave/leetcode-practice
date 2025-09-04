# Time: O(n) -> depends on the size of n argument
# Space: O(1) -> no new structures are created or even used 
#-


def climb_stairs(n):
    if n < 4:
        return n
    i, j, k = 4, 3, 2
    while i <= n:
        j, k = j + k, j
        i += 1
        # k = j
    return j

if __name__ == "__main__":
    print(climb_stairs(5))