from cs50 import get_float

def main():
    while True:
        # Get the amount of change owed in dollars
        change = get_float("Change owed: ")
        # Check if the change is non-negative
        if change > 0:
            break

    # Convert change in dollars to cents
    cents = round(change * 100)

    # Calculate the minimum number of coins
    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickels = (cents % 25 % 10) // 5
    pennies = cents % 5

    # Sum up the number of coins
    total_coins = quarters + dimes + nickels + pennies

    # Output the result
    print(total_coins)

if __name__ == "__main__":
    main()

