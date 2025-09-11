# Time: O(n) -> number of loops depends on how many times the column number is divisible by 26 (meaning its updated value != 0)
# Space: O(n) -> creating a string with the number of characters that depends on same as above
#-
# use 26 range + ascii values to add each digit, updating current value each iteration that its not 0

def excel_sheet_column_title(col_num):
    def add_digit(remainder):
        return chr(remainder + 65)

    str_val, curr_num = '', col_num
    while curr_num != 0:
        diviser = (curr_num - 1) % 26
        str_val = add_digit(diviser) + str_val
        curr_num = (curr_num - 1) // 26
    return str_val

if __name__ == "__main__":
    excel_sheet_column_title(703)