def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
        except ValueError:
                pass

def main():
    # Get the height of the pyramid
    height = get_height()

    # Build the pyramid
    for i in range(1, height +1):
        # Print space
        for j in range(height - i):
            print(" ", end="")
        # Print hashes
        for k in range(i):
            print("#", end="")
        # New line
        print()

if __name__ == "__main__":
    main()