# Time: O(n) -> depends on the number passed despite only 1 loop
# Space: O(n) -> create a new list where the size it grows to depends on the size of n
#-
# pretty simple

def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    result

if __name__ == "__main__":
    fizz_buzz()