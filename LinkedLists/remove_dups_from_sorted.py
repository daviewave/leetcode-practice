# Time: O(n) -> depends on number of nodes in LL passed in
# Space: O(1) -> not creating a dummy node just going through the existing one
#- 

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_dups_from_sorted(head):
        curr, prev = head, None
        while curr:
            if prev and prev.val == curr.val:
                next = curr.next
                prev.next = next
                curr.next = None
                curr = next
            else:
                prev = curr
                curr = curr.next
        return head

if __name__ == "__main__":
    function()