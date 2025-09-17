# Time: O(n)
# Space: O(n)
#-


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_mappings, t_mappings = {}, {}
    for i in range(len(s)):
        if s[i] in s_mappings and s_mappings[s[i]] != t[i]:
            return False
        elif t[i] in t_mappings and t_mappings[t[i]] != s[i]:
            return False
        else:
            s_mappings[s[i]] = t[i]
            t_mappings[t[i]] = s[i]
    return True

if __name__ == "__main__":
    is_isomorphic("add", "egg")