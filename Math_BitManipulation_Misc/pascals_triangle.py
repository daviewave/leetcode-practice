# Time: O(n²) -> has to loop 2x, one loop for each number of rows and one for the calculations on the new row 
# Space: O(n²) -> creating a new array to store each row, which is another array (array of arrays)
#-

def pascals_triangle(num_rows):
    if not num_rows or num_rows < 1:
        return []
    
    def add_row(prev_row):       
        new_row = [1] * (len(prev_row) + 1)
        if len(prev_row) == 1:
            return new_row
        
        i = len(new_row) - 2
        while i - 1 >= 0:
            new_row[i] = prev_row[i] + prev_row[i - 1]
            i -= 1
        return new_row

    res = []
    for i in range(1, num_rows + 1):
        if i == 1:
            res.append([1])
        else:
            res.append(add_row(res[-1]))
    return res
        

if __name__ == "__main__":
    pascals_triangle(5)