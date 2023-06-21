from cs50 import get_string

def main():
    # Get the text from the user
    text = get_string("Text: ")

    # Count the number of letters, words, and sentences
    num_letters = sum(c.isalpha() for c in text)
    num_words = sum(c.isspace() for c in text) + 1
    num_sentences = text.count(".") + text.count("!") + text.count("?")

    # Calculate the average number of letters and sentences per 100 words
    L = (num_letters / num_words) * 100
    S = (num_sentences / num_words) * 100

    # Caculate the Coleman-Liau index
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Output the grade level
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()