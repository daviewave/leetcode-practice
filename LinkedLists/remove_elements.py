# Time: O(n)
# Space: O(1)
#-


def remove_elements(head, val):
    if not head:
        return None
    
    curr, prev = head, None
    while curr:
        next = curr.next
        if curr.val != val:
            prev = curr
        else:
            if prev:
                prev.next = next
                curr.next = None
            else:
                head = next
        curr = next                    
    return head

if __name__ == "__main__":
    remove_elements()