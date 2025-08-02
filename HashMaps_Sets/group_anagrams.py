# Time: O(n * k log k)
# Space: O(n * k)
from collections import defaultdict
def group_anagrams_sorted_key(strs: list):
    groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# Time: O(n * k)
# Space: O(n * k)
def group_anagrams_tuple_count(strs: list):
    if len(strs) < 2:
        return [strs]
    
    groups = {}
    for word in strs:
        letter_frequency = [0] * 26
        for char in word:
            letter_frequency[ord(char) - ord('a')] += 1
        word_key = tuple(letter_frequency)

        if word_key not in groups:
            groups[word_key] = []
        groups[word_key].append(word)

    return list(groups.values())

    


if __name__ == "__main__":
    group_anagrams()