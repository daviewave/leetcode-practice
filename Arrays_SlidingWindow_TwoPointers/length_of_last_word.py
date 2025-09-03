# Time: O(n)
# Space: O(1)
#-

def length_of_last_word(s):
    i, j = len(s) - 1, 0
    while i >= 0:
        if s[i] == " ":
            if j != 0:
                return j
            else:
                i -= 1
                continue
        i -= 1
        j += 1
    return j

if __name__ == "__main__":
    function()