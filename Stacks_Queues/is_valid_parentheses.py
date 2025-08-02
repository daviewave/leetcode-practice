# Time: O(n) -> depends on the size of the string passed as an argument
# Space: O(n) -> stack is dependent on how much is put into it so
#-
# since the requirement means that for every last open value must be the first one closed 
# this mimics stack behavior, so when looping through the string if its an open parentheses
# simply add it to the stack, if its a closed parentheses get the most recent open value
# by popping from the stack and determine if it is properly closed, continuing if so or returning
# false if not. for scenarios where there is only open brackets the loop will finish but
# stack should be empty otherwise there are unmatched opens

def is_valid_parentheses(s):
    stack = []
    for c in s:
        # check if its open
        if c in ["(", "[", "{"]:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            
            top = stack.pop()
            if top == "(" and c == ")":
                continue
            elif top == "[" and c == "]":
                continue
            elif top == "{" and c == "}":
                continue
            else:
                return False
    return len(stack) == 0

        

if __name__ == "__main__":
    is_valid_parentheses()