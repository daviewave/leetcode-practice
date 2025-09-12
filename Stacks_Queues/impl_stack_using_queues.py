# Time: 
# Space:
#- 
# each time and space depends on the function but they are all O(1) since deque is faster than regular python list methods  

from collections import deque
class MyStack:
    def __init__(self):
        self.data = deque([])

    def push(self, x: int) -> None:
        self.data.appendleft(x)

    def pop(self) -> int:
        return self.data.popleft()

    def top(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return len(self.data) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(x=2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()