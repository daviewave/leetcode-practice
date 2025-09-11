# Time: O(n) -> depends on the number of characters in the column title string passed in 
# Space: O(1) -> only using simple int variables to track index and current total
#-

def excel_sheet_column_number(col_title):
    i, total = 0, 0
    while i < len(col_title):
        letter_val = ord(col_title[i]) - 64
        total = total * 26 + letter_val 
        i += 1
    return total

if __name__ == "__main__":
    excel_sheet_column_number("AAZ")