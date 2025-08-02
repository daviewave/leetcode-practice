# Time: 
# Space:
#-
# 
# 
# 

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if head and head.next is head:
        return False
    
    slow, fast = head, head
    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False        


if __name__ == "__main__":
    has_cycle()



#- notes -#
#-> some how track the position of the head
#-> no node can have a next value of none
