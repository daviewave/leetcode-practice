# Time: O(n) -> depends on the size of the linked list
# Space: O(1) -> no new data structures, just manipulating the one passed in
#-
# since the end of the starting LL will have a next value of None, we want the current head to 
# take over that role, but before doing that we need to store the value of the heads next node
# so it's next value can then be pointed to the head, and after update the new placeholder 
# current and previous values

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_singly(head):
    current = head
    prev = None

    while current: #is not None
        next = current.next
        current.next = prev
        prev = current
        current = next


if __name__ == "__main__":
    ln_1 = ListNode(1, 2)
    ln_2 = ListNode(2, 3)
    ln_3 = ListNode(3, 4)
    ln_4 = ListNode(4, 5)
    ln_5 = ListNode(5, 6)
    ln_6 = ListNode(6)
    
    reverse_singly([ln_1, ln_2, ln_3, ln_4, ln_5, ln_6])