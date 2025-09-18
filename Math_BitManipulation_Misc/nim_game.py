# Time:  O(1)
# Space: O(1)
#-


def nim_game(n):
    return n % 4 != 0

if __name__ == "__main__":
    nim_game(8)