# Time: O(n) -> depends on the size of the strings passed in
# Space: O(1) -> although a new data structure is created its a constant size
#-
# 1, init fixed are for each alphabet letter
# 2, loop through the 'zipped' result of each string, which allows each index's letter to be analyzed in same loop
# 3, increase or decrease the count of each letters relative location on the const array initialized by subtracting the ordinal
#       number of the current character - the smallest ordinal number in alphabet a so that each letter will be counted in its correct location in the const
#       array, one string increases while the other decreases in attempt to cancel each other out, which would mean they have the same number of letters
# 4, determine if each count has been cancelled out (is 0) and return True if so, False otherwise


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    letter_frequencies = [0] * 26 # init fixed are for each alpha letter
    for s_char, t_char in zip(s, t):
        letter_frequencies[ord(s_char) - ord('a')] += 1
        letter_frequencies[ord(t_char) - ord('a')] -= 1

    return all(freq == 0 for freq in letter_frequencies)

if __name__ == "__main__":
    valid_anagram()