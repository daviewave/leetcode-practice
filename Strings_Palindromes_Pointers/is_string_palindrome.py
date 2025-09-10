# Time: O(n) -> loops through string to clean it so depends on size of string
# Space: O(n) -> created a new string
#-


def is_string_palindrome(s):
    if len(s) < 2:
        return True

    cleaned = " ".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    is_string_palindrome()