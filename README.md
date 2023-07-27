# CS50: Introduction to Computer Science and Programming

CS50 is an introductory course provided by Harvard University, designed to immerse students in the intellectual fields of computer science and programming. It caters to individuals with or without prior experience, focusing on computational thinking, problem-solving, abstraction, algorithms, and data structures. The course starts with the C language, progressing towards Python, SQL, HTML, CSS, and JavaScript, and culminates with a final project.

The course includes 10 Problem Sets, 9 Labs, and 1 Final Project.

# CS50-Assignments-Solutuons

# Lab 1: Population Growth

## Objective
This program calculates the number of years required for a population to grow from a start size to an end size.

## Instructions
1. Prompt the user for a starting population size. If a number less than 9 is entered (the minimum allowed population size), prompt again until a number greater than or equal to 9 is entered.
2. Prompt the user for an ending population size. If a number less than the starting population size is entered, prompt again until a number greater than or equal to the starting population size is entered.
3. Calculate the (integer) number of years required for the population to reach at least the size of the end value.
4. Print the number of years required for the population to reach the end size, as by printing to the terminal `Years: n`, where `n` is the number of years.

## Expected Output
An integer value representing the number of years it will take for the population to grow from the start size to the end size.

# Problem Set 1: Exercise 1 - Hello

## Objective
The goal of this exercise is to create a simple C program that prints "Hello, world" to the console.

## Instructions
1. Execute `code hello.c` to create a new file called hello.c in your codespace’s text editor.
2. Write the following lines into `hello.c`:

include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}

# Problem Set 1: Exercise 1 - Hello

## Objective
This exercise aims to recreate a right-aligned pyramid of blocks from the Nintendo's Super Mario Brothers, using hashes (#) for bricks. The pyramid's height will be determined by user input.

## Instructions
1. Open the file called `mario.c` inside of your mario directory.
2. Modify `mario.c` to prompt the user for the pyramid’s height, storing their input in a variable. Re-prompt the user as needed if their input is not a positive integer between 1 and 8, inclusive.
3. Print the value of that variable to confirm that you've stored the user's input successfully.
4. Modify the program so that it doesn't just print the user’s input but prints a left-aligned pyramid of the specified height.
5. Finally, modify the pyramid to be right-aligned by prefixing the hashes with dots (i.e., periods).

## Expected Output
A right-aligned pyramid of hashes, the height of which is determined by the user's input.

# Exercise 3: Cash Change

## Objective
In this exercise, you will complete a program that calculates the smallest number of coins required to give a customer their change.

## Instructions
1. Complete the function `get_cents` that prompts the user for a number of cents using `get_int` and returns that number as an `int`. If the user inputs a negative `int`, your code should prompt the user again.
2. Implement `calculate_quarters` such that it calculates and returns as an `int`, how many quarters a customer should be given if they’re owed some number of cents.
3. Implement `calculate_dimes` to calculate and return the number of dimes the customer should be given.
4. Implement `calculate_nickels` to calculate and return the number of nickels the customer should be given.
5. Implement `calculate_pennies` to calculate and return the number of pennies the customer should be given.

## Note
Each `calculate` function should accept any value of cents, not just those values that the greedy algorithm might suggest. For instance, if cents is 85, `calculate_dimes` should return 8.

## Expected Output
The smallest number of coins required to give a customer their change.

# Lab 2: Scrabble

## Objective
This lab implements a simplified game of Scrabble where two players enter their words, and the player with the higher-scoring word wins.

## Instructions
1. Complete the implementation of `scrabble.c`. We've already stored the point values of each letter of the alphabet in an integer array named `POINTS`.
2. Implement a helper function `compute_score()` that takes a string as input and returns an `int`. This function should compute the score for the string argument using the `POINTS` array.
3. Characters that are not letters should be given zero points, and uppercase and lowercase letters should be given the same point values.
4. No need to check if a word is in the dictionary for this problem.
5. In `main()`, your program should print out the winner depending on the players' scores. If it's a tie, print `Tie!`.

## Note
The `get_string()` function is used to prompt the two players for their words. These values are stored inside variables named `word1` and `word2`.

## Expected Output
The program prints `Player 1 wins!`, `Player 2 wins!`, or `Tie!`, depending on the scores of the players.

# Problem Set 2: Bulbs

## Objective
This problem set involves writing a program, `bulbs`, that takes a message and converts it to a sequence of binary numbers representing light bulb states (on/off). 

## Understanding Bases
Computers use base-2, or binary. Each digit in a binary number can only be a 0 or a 1. A binary number can be converted to a decimal number using the power of 2. For example, the binary number 10101 in base-2 represents 16 + 0 + 4 + 0 + 1, which is equal to the decimal number 21.

## Encoding a Message
1. Convert the text into decimal numbers using the ASCII standard. For example, 'H' is represented by the decimal number 72, 'I' is represented by 73, and '!' is represented by 33.
2. Convert these decimal numbers into equivalent binary numbers. Assume each decimal number is represented with 8 bits. For example, 72 is represented in binary as 01001000, 73 as 01001001, and 33 as 00100001.
3. Interpret these binary numbers as instructions for the light bulbs on stage; 0 represents 'off', 1 represents 'on'. Note: `bulbs.c` includes a `print_bulb` function that outputs emoji representing light bulbs, given a 0 or 1.

## Expected Output
The program should print out the binary equivalent of the input string with each character represented as a sequence of eight light bulb emojis, where an 'on' bulb represents '1' and an 'off' bulb represents '0'.

# Lab 3: Sort

## Objective
This lab involves determining which sorting algorithm (selection sort, bubble sort, or merge sort) is implemented by three provided, already-compiled C programs: `sort1`, `sort2`, and `sort3`.

## Instructions
1. Run the `sort1`, `sort2`, and `sort3` programs on different lists of values provided in .txt files. These files contain lines of numbers that are either reversed, shuffled, or sorted.
2. Use the command `./[program_name] [text_file.txt]` to run the sorting programs on the text files. Replace `[program_name]` with `sort1`, `sort2`, or `sort3` and `[text_file.txt]` with the name of the file you wish to sort.
3. You can time your sorts by running `time ./[sort_file] [text_file.txt]`. Look at the `real time` in the terminal's output to see how much time actually elapsed while running the program.
4. Based on your observations, determine which sorting algorithm each program uses.

## Deliverables
Record your answers and explanations for each program in `answers.txt`, filling in the blanks marked TODO.

# Problem Set 3: Plurality
This program simulates a plurality vote election using C. 

## Understanding the Program

- A struct `candidate` is defined, representing a candidate with a `name` and `votes`.
- A global array `candidates` is maintained with each element as a `candidate`.
- The `main` function sets a global variable `candidate_count`, copies the command-line arguments into `candidates`, prompts user for number of voters, collects votes, and finally calls `print_winner`.

## Key Functions

- `vote`: Should update the vote count for a valid voted candidate and return true. Returns false for an invalid candidate.
- `print_winner`: Should print the candidate(s) with the most votes.

## Execution

1. Compile with `make plurality` or `clang -o plurality plurality.c -lcs50`.
2. Execute with `./plurality [Candidate Names]`.
3. Follow prompts to input number of voters and their votes.

# Problem Set 3: Runoff
This program simulates a runoff voting election using C. 

## Understanding the Program

- Two constants: `MAX_CANDIDATES` and `MAX_VOTERS` represent the maximum number of candidates and voters respectively.
- The two-dimensional array `preferences[i][j]` stores the index of the candidate who is the `j`th preference for voter `i`.
- A struct `candidate` is defined with fields: `name`, `votes` (number of votes the candidate has), and `eliminated` (boolean indicating if the candidate has been eliminated).
- The `candidates` array keeps track of all the candidates in the election.
- Two global variables: `voter_count` and `candidate_count`.

## Key Functions

- `vote`: Records preferences if vote is valid.
- `tabulate`: Computes votes based on top choice candidates.
- `print_winner`: Prints winner of the election if one exists.
- `find_min`: Finds minimum number of votes a candidate has.
- `is_tie`: Determines if the election is a tie.
- `eliminate`: Eliminates candidate (or candidates) in last place.

## Execution

1. Compile with `make runoff` or `clang -o runoff runoff.c -lcs50`.
2. Execute with `./runoff [Candidate Names]`.
3. Follow prompts to input number of voters and their votes.

# Lab 4: Smiley

In this lab, we'll change the color of black pixels in a bitmap image. 

## Understanding 

The provided C code in `helpers.c` contains an incomplete function `colorize`. The function accepts the image's height, width, and a two-dimensional array of pixels.

Our task is to implement this function such that it changes all the black pixels in the image to a color of our choosing.

# Problem Set 4 Exercise 1: Filter

This exercise involves implementing several image filtering algorithms. Each function in `helpers.c` applies a different filter to an input image.

## Understanding

There are four filters to implement:

1. **Grayscale:** The `grayscale` function should convert the image into a black-and-white version of itself.
2. **Sepia:** The `sepia` function should convert the image into a sepia version of itself.
3. **Reflection:** The `reflect` function should reflect the image horizontally.
4. **Blur:** The `blur` function should convert the image into a box-blurred version of itself.

# Problem Set 4 Exercise 2: Recover

This exercise involves implementing a program to recover JPEG images from a forensic image. Your implementation should be in a file named `recover.c`.

## Understanding

The task is to implement a program named `recover` that recovers JPEGs from a forensic image. Here are the specifications:

- The program should accept exactly one command-line argument: the name of a forensic image from which to recover JPEGs.
- If the program is not executed with exactly one command-line argument, it should remind the user of correct usage, and `main` should return 1.
- If the forensic image cannot be opened for reading, your program should inform the user as much, and `main` should return 1.
- The files you generate should each be named `###.jpg`, where `###` is a three-digit decimal number, starting with `000` for the first image and counting up.
- Your program, if it uses `malloc`, must not leak any memory.

Note: The function signatures in `helpers.c` should not be modified, nor should any other files be modified.

# Lab 5: Inheritance

This lab involves creating a program that models genetic inheritance, allocating memory for a family, assigning blood type alleles, and freeing memory when done.

## Understanding

The task is to complete the implementation of `inheritance.c`. This program creates a family of a specified generation size and assigns blood type alleles to each family member. The oldest generation will have alleles assigned randomly.

The `create_family` function takes an integer (`generations`) as input and should allocate one person for each member of the family of that number of generations. It should return a pointer to the person in the youngest generation.

Each person should have alleles and parents assigned to them. The oldest generation should have both alleles randomly chosen and both parents set to NULL. Younger generations should inherit one allele (chosen at random) from each parent and have an array of two pointers, each pointing to a different parent.

The `free_family` function should accept as input a pointer to a person, free memory for that person, and then recursively free memory for all of their ancestors.

# Problem Set 5: Speller

This problem set involves implementing a spell-checking program using a hash table. The goal is to create the functions `load`, `hash`, `size`, `check`, and `unload` as efficiently as possible.

## Understanding

The spell-checking program is called "speller". Its efficiency depends on how well the functions for handling the hash table are implemented.

- `load`: This function loads the dictionary into memory.
- `hash`: This function calculates the hash value for a given word.
- `size`: This function returns the number of words in the dictionary.
- `check`: This function checks if a word is in the dictionary.
- `unload`: This function unloads the dictionary from memory.

The performance of the program is benchmarked based on the time spent in `load`, `check`, `size`, and `unload`.

## Specifications

- You may not alter `speller.c` or `Makefile`.
- You may alter `dictionary.c`, but you may not alter the declarations of `load`, `hash`, `size`, `check`, or `unload`.
- You may change the value of `N` in `dictionary.c` so that your hash table can have more buckets.
- Your implementation of `check` must be case-insensitive.
- Your spell checker may only take `text` and, optionally, `dictionary` as input.
- Your spell checker must not leak any memory.

# Lab 6: World Cup

In this lab, you will be tasked with implementing a program that simulates a number of tournaments and calculates each team's probability of winning. The program is written in Python and requires the use of the `csv` module to read team data from a CSV file.

## Understanding

The program will simulate a series of football tournaments, with the teams and their respective ratings given in a CSV file. The program should then output the probability of each team winning the tournament.

# Problem Set 6 Exercise 1: Mario

This exercise invites you to create a Python program in a file called `mario.py`. Your task is to recreate the half-pyramid made of hashes (#) just like you did in Problem Set 1, but this time in Python. 

The detailed steps are as follows:

1. Prompt the user for the half-pyramid's height, which should be a positive integer between 1 and 8, inclusive. This can be done using the `get_int` function.

2. If the user provides an input outside of the valid range, you need to re-prompt them until a valid input is received.

3. Using the `print` function and one or more loops, generate the desired half-pyramid.

4. Make sure to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.

# Problem Set 6 Exercise 2: Cash
In this exercise, you will create a Python program in a file called `cash.py`. The program will first prompt the user to enter the amount of change owed and then determine the minimum number of coins needed to make that change.

Here are the detailed steps to follow:

1. Use the `get_float` function from the CS50 Library to get the user’s input. The input should be in dollars (e.g., 0.50 dollars instead of 50 cents).

2. Assume the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).

3. If the user provides a negative value, re-prompt the user for a valid amount until they enter a non-negative value.

4. The last line of output from your program should be the minimum number of coins possible. This should be an integer followed by a newline.

# Problem Set 6 Exercise 3: Readability
This is a simple Python script that calculates the readability of a text input by a user. It uses the Coleman-Liau index formula, which is a readability test designed to gauge the understandability of a text. 

## Description

The script prompts the user to input a text. It then calculates the number of letters, words, and sentences in the text, and outputs the readability grade. 

A 'letter' is considered to be any lowercase or uppercase character from 'a' to 'z'. A 'word' is any sequence of characters separated by spaces, and a 'sentence' ends with a period, exclamation point, or question mark.

The formula for the Coleman-Liau index is `0.0588 * L - 0.296 * S - 15.8`, where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

# Lab 7: Songs

This lab involves executing various SQL queries on a songs database. Here's a summary of the tasks:

1. List the names of all songs in the database. File: `1.sql`.
2. List the names of all songs in increasing order of tempo. File: `2.sql`.
3. List the names of the top 5 longest songs, in descending order of length. File: `3.sql`.
4. List the names of any songs that have danceability, energy, and valence greater than 0.75. File: `4.sql`.
5. Return the average energy of all the songs. File: `5.sql`.
6. List the names of songs that are by Post Malone. File: `6.sql`.
7. Return the average energy of songs that are by Drake. File: `7.sql`.
8. List the names of the songs that feature other artists. File: `8.sql`.

## Notes

1. All queries should return only the data necessary to answer the question.
2. No assumptions are made about the ids of any particular songs or artists.
3. The database structure, i.e., table names and column names, should be accurately known to execute these queries.

# Problem Set 7: Exercise 1: Movies

This problem set involves executing various SQL queries on a movies database. The tasks for each exercise are:

1. List the titles of all movies released in 2008. File: `1.sql`.
2. Determine the birth year of Emma Stone. File: `2.sql`.
3. List the titles of all movies with a release date on or after 2018, in alphabetical order. File: `3.sql`.
4. Determine the number of movies with an IMDb rating of 10.0. File: `4.sql`.
5. List the titles and release years of all Harry Potter movies, in chronological order. File: `5.sql`.
6. Determine the average rating of all movies released in 2012. File: `6.sql`.
7. List all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title. File: `7.sql`.
8. List the names of all people who starred in Toy Story. File: `8.sql`.
9. List the names of all people who starred in a movie released in 2004, ordered by birth year. File: `9.sql`.
10. List the names of all people who have directed a movie that received a rating of at least 9.0. File: `10.sql`.
11. List the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated. File: `11.sql`.
12. List the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred. File: `12.sql`.
13. List the names of all people who starred in a movie in which Kevin Bacon also starred. File: `13.sql`.

## Notes

1. All queries should return only the data necessary to answer the question.
2. No assumptions are made about the ids of any particular movies or people.
3. The database structure, i.e., table names and column names, should be accurately known to execute these queries.

# Problem Set 7: Exercise 5: Fiftyville
The famous CS50 Duck has been stolen! The thief absconded quickly after the crime, fleeing the town of Fiftyville. To aid in cracking this case, you will be provided with a SQLite database (`fiftyville.db`) containing relevant records from around the time of the theft.

Your mission, should you choose to accept it, is to solve the following:

1. Identify the thief.
2. Determine the city to which the thief escaped.
3. Uncover the accomplice who facilitated the thief's escape.

The theft took place on July 28, 2021, on Humphrey Street in Fiftyville.

As part of your investigation, document each SQL query in the `log.sql` file, preceded by a comment explaining the reasoning behind each query or the information you hope to derive from it. The purpose of these queries and comments is to provide a clear roadmap of your thought process and investigative methodology. Be sure to follow best practices for SQL style and readability, as outlined in [sqlstyle.guide](http://www.sqlstyle.guide/), particularly the indentation section.

Upon solving the mystery, fill in the provided `answers.txt` file with the name of the thief, the city to which they escaped, and the name of their accomplice. Make sure not to modify any existing text or add additional lines.

## Notes

1. All queries should be executed on the `fiftyville.db` database.
2. This problem set emphasizes the process of solving the mystery as much as the solution itself.

# Lab 8: Trivia

Welcome to Trivia Lab! In this lab, you will design a webpage using HTML, CSS, and JavaScript to let users answer trivia questions.

## Requirements

1. In `index.html`, beneath "Part 1", add a multiple-choice trivia question of your choosing with HTML. Use an `h3` heading for the text of your question. Provide at least three answer choices in the form of buttons, only one of which should be correct.

2. Using JavaScript, implement logic so that the buttons change colors when a user clicks on them. If a user clicks on a button with an incorrect answer, the button should turn red and "Incorrect" should appear beneath the question. If the user clicks on the correct answer, the button should turn green and "Correct!" should appear beneath the question.

3. In `index.html`, beneath "Part 2", add a text-based free response question of your choosing with HTML. Use an `h3` heading for the text of your question. Use an input field to allow the user to type a response, and a button for the user to confirm their answer.

4. Using JavaScript, add logic so that the text field changes color when a user confirms their answer. If the user types an incorrect answer and presses the confirmation button, the text field should turn red and "Incorrect" should appear beneath the question. If the user types the correct answer and presses the confirmation button, the input field should turn green and "Correct!" should appear beneath the question.

## Optional Tasks

1. Edit `styles.css` to change the CSS of your webpage.
2. Add additional trivia questions to your trivia quiz.

# Problem Set 8: Homepage

Welcome to the Homepage Problem Set! In this assignment, you will be tasked with building a simple homepage using HTML, CSS, and JavaScript. This is a great opportunity to apply your web development skills and creativity.

## Requirements

1. The website must contain at least four different `.html` pages, one of which should be `index.html` (the main page of your website). It should be possible to navigate from any page on your website to any other page by following one or more hyperlinks.

2. Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!

3. Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library that comes with lots of CSS classes and more to help you beautify your site. See [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to get started.

4. Create at least one stylesheet file named `styles.css`. It should use at least five (5) different CSS selectors (e.g. tag (example), class (.example), or ID (#example)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`.

5. Integrate one or more features of JavaScript into your site to make it more interactive. For example, you could use JavaScript to add alerts, to have an effect at a recurring interval, or to add interactivity to buttons, dropdowns, or forms. Feel free to be creative!

6. Make sure your site looks nice on browsers both on mobile devices and on laptops and desktops. This will require you to consider responsive design in your CSS.

# Lab 9: Birthdays

In this lab, we will create a simple web application to store and track friends' birthdays.

## Objectives:
- Get hands-on experience with Flask, a web framework for Python.
- Gain practice with SQLite to manage a database of birthdays.

## Overview:
Our web application has a simple objective: keep track of friends' birthdays.

The application handles two types of requests:
1. GET request to the '/' route: The app displays all the stored birthdays in a tabular format.
2. POST request to the '/' route: The app adds a new entry to the birthdays database and re-renders the index page.

## How to Run the App:
1. Set up the SQLite database named `birthdays.db`.
2. Add logic in `app.py` for handling GET requests to query the `birthdays.db` database for all birthdays and pass all of that data to your `index.html` template.
3. Add logic in `index.html` to render each birthday as a row in the table.
4. Add an HTML form in `index.html` to capture user inputs for name, birthday month, and birthday day.
5. Add logic in `app.py` for handling POST requests to insert a new row into the `birthdays` table based on the data supplied by the user.

# Problem Set 9: Finance

In this problem set, we will create a mock stock trading website.

## Objectives:
- Get hands-on experience with Flask, a web framework for Python.
- Learn and practice SQLite to manage a user database.
- Implement real-time stock quote information using IEX Cloud's API.
- Understand and practice basic concepts of finance and stock trading.

## Overview:

This web application simulates the following functionalities of a stock trading website:

### Register:

Users can register an account by providing a username and password. The password is hashed before it's stored in the SQLite database for security.

### Quote:

Users can look up a stock's current price by inputting the stock's symbol.

### Buy:

Users can buy stocks by providing the stock's symbol and the number of shares they wish to buy. The total price of the stock is deducted from the user's cash balance.

### Index:

The index page displays an HTML table summarizing the stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding. The user's current cash balance and the grand total is also displayed.

### Sell:

Users can sell shares of a stock that they own by inputting the stock's symbol and the number of shares they wish to sell.

### History:

The history page displays an HTML table summarizing all of the user's transactions, including both purchases and sales of stocks.

## How to Run the App:

1. Set up the SQLite database.
2. Use the `generate_password_hash` and `check_password_hash` functions from the Werkzeug library for handling user registration and login.
3. Use the `lookup` function to interact with the IEX Cloud API for real-time stock data.
4. Use SQLite to manage user data and transaction history.
