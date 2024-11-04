def main():
    
    foods = ['pizza','burger','taco']
    print(*foods)
    item = input("what do you want to change? ")
    try:
        item_index = foods.index(item)
        new_item = input("what's the new food? ")
        foods[item_index] = new_item
    except ValueError as err:
        print(err)
    finally:
        print(*foods)
    
main()
