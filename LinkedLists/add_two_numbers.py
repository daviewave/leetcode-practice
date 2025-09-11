# Time: O(m + n) -> loops through the entireity of each linked list passed in so depends on the size of each
# Space: O(m + n) with O(1) extra space -> new linked list size that will be returned depends on the size of the 2 passed in
#-


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_two_numbers_efficient(l1, l2):
        carry = 0
        prev, head = None, None
        while l1 or l2:
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next

            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            new_val = (l1_val + l2_val) + carry
            carry = 0 if new_val < 10 else 1
            
            new_node = ListNode(val=new_val % 10)
            if prev:
                prev.next = new_node
            else:
                head = new_node
            prev = new_node
    
        if carry == 1:
            new_node = ListNode(val=1)
            prev.next = new_node
        return head


def add_two_numbers_first_attempt_simple(l1, l2):
    num1, num2 = '', ''
    curr1, curr2 = l1, l2
    while curr1 or curr2:
        if curr1:
            num1 = str(curr1.val) + num1
            curr1 = curr1.next
        if curr2:
            num2 = str(curr2.val) + num2
            curr2 = curr2.next

    res = str(int(num1) + int(num2))
    i = len(res) - 1
    prev_node, head = None, None
    while i >= 0:
        new_node = ListNode(int(res[i]))
        if prev_node:
            prev_node.next = new_node
        else:
            head = new_node
        prev_node = new_node
        i -= 1
    return head

if __name__ == "__main__":
    add_two_numbers()