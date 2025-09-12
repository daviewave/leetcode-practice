# Time: 
# Space:
#-

from collections import deque
class MyQueue:
    def __init__(self):
        self.data = deque([])

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.popleft()

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return len(self.data) == 0

if __name__ == "__main__":
    function()