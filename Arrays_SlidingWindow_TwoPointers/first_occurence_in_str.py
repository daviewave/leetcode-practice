# Time: O(n x m) -> only loops through the "haystack" string once but depends on the size of the string  
# Space: O(1) -> no new data structures created
#-

def first_occurence_in_str_mine(haystack, needle):
    j, k = 0, -1
    for i in range(len(haystack)):
        if haystack[i] == needle[j]:
            if j == 0:
                k = i
            j += 1
            if j == len(needle):
                return k       
        else:
            if j > 0:
                i = k
                j, k = 0, -1
            else:
                j, k = 0, -1
    return -1

# Time: O(n + m) -> only loops through the "haystack" string once but depends on the size of the string  
# Space: O(1) -> no new data structures created
#-
# since the solution provided above will reset the 'i' index to the beginning of the prefix found everytime there is a mismatch it results in unnesessary re-checks. using the KMP algorythim first finds the longest prefix suffix (lps) so when the looping search begins for the haystack, if a mismatch occurs the current index will be reset to the previous longest prefix suffix.

def first_occurence_in_str_kmp(haystack, needle):
    if not needle or not haystack:
        return -1

    lps = [0] * len(needle)
    length = 0
    i = 1
    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

if __name__ == "__main__":
    print(first_occurence_in_str_mine("aaaab", "aab"))