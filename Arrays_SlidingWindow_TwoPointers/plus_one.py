# Time: O(n)
# Space: O(1)
#-


def plus_one(digits):
    i = len(digits) - 1
    while True:
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                return digits                    
            i -= 1

if __name__ == "__main__":
    plus_one([1, 2, 3])