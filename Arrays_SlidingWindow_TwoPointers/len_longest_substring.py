# Time: O(n)
# Space: O(n)
#-
# clearing the set causes the time to jump to O(n^2) so redid it with true sliding window method that only uses 1 set

def len_longest_substring_sliding_window(s):
    if len(s) < 2:
        return len(s)

    i, longest = 0, 1
    seen = set(s[i])
    for j in range(1, len(s)):
        if s[j] not in seen:
            seen.add(s[j])
            longest = max(longest, len(seen))
        else:
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
    return longest

def len_longest_substring_inefficient(s):
    if len(s) < 2:
        return len(s)

    seen = set()
    i, j, longest = 0, 1, 1
    while j < len(s):
        seen.add(s[i])
        if s[j] not in seen:
            seen.add(s[j])
            longest = len(seen) if len(seen) > longest else longest
            j += 1
        else:
            i += 1
            j = i + 1
            seen.clear()
    longest = len(seen) if len(seen) > longest else longest
    return longest

if __name__ == "__main__":
    len_longest_substring()