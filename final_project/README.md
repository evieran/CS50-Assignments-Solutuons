# Cognitive Distortion Identifier
#### Video Demo:  <URL HERE>

#### Description:
Cognitive Distortion Identifier is a web application designed to help individuals identify and understand cognitive distortions in their thoughts. Cognitive distortions are irrational thought patterns that contribute to anxiety, depression, and other mental health issues. Through this application, users can gain insights into their thinking patterns and receive suggestions to reframe their thoughts.

# Features
## Features
- **User Registration and Authentication**: New users can register for an account and login to use the application.
- **Thought Input**: Users can input their thoughts or statements.
- **Distortion Identification**: The application analyzes the thoughts to identify common cognitive distortions such as “black-and-white thinking”, “overgeneralization”, or “catastrophizing”.
- **Explanation and Education**: Upon identifying a cognitive distortion, the application provides an explanation and information on its negative impact on emotions or behavior.
- **Reframing Suggestions**: The application suggests more balanced or rational ways to think about situations.
- **Daily Tips and Challenges**: The application presents daily tips and challenges for personal growth and positive thinking.
- **Progress Tracking**: The application tracks and records the types of cognitive distortions encountered, allowing users to observe patterns in their thinking over time.


# Getting Started
## Prerequisites
- Python 3.x
- Flask web framework

## Installing
1. Clone this repository to your local machine.
git clone <repository_url>

2. Navigate to the project directory.
cd cognitive-distortion-identifier

3. Install the required packages.
pip install -r requirements.txt

4. Set up the Flask environment variables.
export FLASK_APP=app.py
export FLASK_ENV=development

5. Run the Flask application.
flask run

6. Access the application in your web browser at http://127.0.0.1:5000.

## The Users See:
- "This tool helps to identify cognitive distortions in your thoughts. Cognitive distortions are irrational thought patterns that can contribute to mental health issues such as anxiety and depression."
- "Tip of The Day"
- Personalized Feedback to their Thought Input
- They can select a "Challenge of the Day"

## How to Use
1. **Registration and Login**: Register for a new account and log in.
2. **Enter Your Thoughts**: Type your thoughts or statements in the text input area.
3. **Identify Distortions**: The application analyzes your input to identify cognitive distortions.
4. **Read Explanation and Reframe Suggestions**: If a cognitive distortion is identified, you’ll receive an explanation of the distortion and suggestions on how to reframe it.
5. **Engage with Daily Tips and Challenges**: View daily tips and participate in the challenge of the day.
6. **Track Your Progress**: The application keeps track of the types of distortions you encounter, allowing you to observe patterns in your thought process over time.
7. **Continuous Improvement**: Use the insights gained to improve your thought patterns and mental well-being.

## Design Choices
The application employs Flask for its simplicity and ease of use. User authentication was implemented to create a personalized experience for each user. The cognitive distortion identification logic is based on keyword analysis. This approach was chosen for its simplicity as a proof of concept, although more sophisticated natural language processing techniques could be employed for greater accuracy in a future version of the application.

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

- Where I get CS50 course?
https://cs50.harvard.edu/x/2020/

## Acknowledgements
Flask Web Framework
Bootstrap for styling