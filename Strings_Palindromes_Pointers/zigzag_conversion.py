# Time: O(n)
# Space: O(n)
#-


def zigzag_conversion(s, num_rows):
    if num_rows == 1:
        return s

    rows = [''] * num_rows
    dcount, ucount = 0, num_rows - 2 
    down = True
    for i in range(len(s)):
        if down or num_rows == 2:
            rows[dcount] = rows[dcount] + s[i]
            dcount += 1
            if dcount == num_rows:
                dcount = 0
                down = False
        else:
            rows[ucount] = rows[ucount] + s[i]
            ucount -= 1
            if ucount == 0:
                ucount = num_rows - 2
                down = True
    return "".join(rows)

if __name__ == "__main__":
    zigzag_conversion("ABCDEF")