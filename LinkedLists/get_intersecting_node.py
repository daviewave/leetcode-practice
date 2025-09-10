# Time: O(m + n) -> depends on the length of length of both list A and list B as it will loop through each completely if no intersection 
# Space: O(1) -> no new data structures needed other than pointer variables to the current node in list A and list B
#-
# Problem is asking if there is an intersecting node meaning the same node in memory versus 2 nodes having the same value, so using while 'is not' will compare complete structures as they are stored in memory so loop through each until None then set the current node to the head of the other list, allowing the comparison to continue until looped through each node the same number of times

def get_intersecting_node(head_a, head_b):
    if not head_a or not head_b:
        return False

    curr_a, curr_b = head_a, head_b
    while curr_a is not curr_b:
        curr_a = curr_a.next if curr_a else head_b
        curr_b = curr_b.next if curr_b else head_a
    return curr_a

if __name__ == "__main__":
    get_intersecting_node()