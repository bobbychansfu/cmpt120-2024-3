import random
ROWS = 3
COLUMNS = 4

def main():
    temp_row = [0]*COLUMNS
    temp_row1 = temp_row[:]
    temp_row2 = temp_row[:]

    values = [temp_row, temp_row1, temp_row2]

    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(1,100)

    print(*values)

main()
