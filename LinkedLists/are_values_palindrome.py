# Time:  O(n)
# Space: O(n)
#-

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def are_values_palindrome(head):
    if not head:
        return True
    
    values = []
    while head:
        values.append(head.val)
        head = head.next

    i, j = 0, len(values) - 1
    while i < j:
        if values[i] != values[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    are_values_palindrome()