# Time: O(n)
# Space: O(n)
#-

def word_pattern(pattern, s):
    strarr = s.split(" ")
    
    if len(pattern) != len(strarr):
        return False

    mappings, seen = {}, set()
    for i in range(len(pattern)):
        if pattern[i] in mappings and mappings[pattern[i]] != strarr[i]:
            return False
        if pattern[i] not in mappings and strarr[i] in seen:
            return False
        mappings[pattern[i]] = strarr[i]
        seen.add(strarr[i])
    return True

if __name__ == "__main__":
    word_pattern()