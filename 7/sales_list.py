NUM_DAYS = 5
WEEK = ["Mon", "Tues", "Wed", "Thurs", "Fri"]

def main():
    sales = [0] * NUM_DAYS
    index = 0

    print("Enter Sales")

    while (index < NUM_DAYS):

        print(WEEK[index],":")
        sales[index] = float(input())
        index += 1

    print()
    print(*sales)

main()
