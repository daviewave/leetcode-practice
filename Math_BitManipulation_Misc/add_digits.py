# Time: O(1)
# Space: O(1)
#-
# use the digital root trick which works because the single digit addition will always return the resulting single digit number other than when the original number is evenly divisible by 9, in which case this means that the single digit is 9 


def add_digits(num):
    if num == 0:
        return 0
    digital_root = num % 9
    return 9 if digital_root == 0 else digital_root

if __name__ == "__main__":
    add_digits(285)