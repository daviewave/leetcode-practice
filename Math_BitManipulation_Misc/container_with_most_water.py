# Time: O(n)
# Space: O(1)
#-


def container_with_most_water(height):
    def calc_area(y2, y1, x2, x1):
        return (y2 - y1) * min(x2, x1)
    
    most = 0
    left, right = 0, len(height) - 1
    while left < right:
        most = max(most, calc_area(right, left, height[right], height[left]))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return most

if __name__ == "__main__":
    container_with_most_water([1,8,6,2,5,4,8,3,7])