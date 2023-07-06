import datetime
import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///yourdatabase.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html", message="Must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("error.html", message="Must provide password")

        # Ensure password and confirmation password are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template("error.html", message="Passwords must match")

        # Hash the user's password
        hash_password = generate_password_hash(request.form.get("password"))

        # Insert the new user into the database
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                            username=request.form.get("username"), hash=hash_password)

        # Check if the username already exists
        if not result:
            return render_template("error.html", message="Username already exists")

        # Log the user in
        session["user_id"] = result

        # Redirect user to home page
        return redirect(url_for("index"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("apology.html", message="must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("apology.html", message="must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("apology.html", message="invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


cognitive_distortions = {
    "black_and_white": {
        "explanation": "Seeing things in only two categories (good or bad, success or failure) without acknowledging any spectrum in between.",
        "reframe": "Consider that things often lie on a spectrum rather than in absolutes."
    },
    "overgeneralization": {
        "explanation": "Making broad interpretations from a single or few events.",
        "reframe": "Recognize that one event does not necessarily represent a consistent pattern."
    },
    "filtering": {
        "explanation": "Focusing on the negative details while ignoring all the positive aspects of a situation.",
        "reframe": "Try to acknowledge and appreciate positive aspects, even in a negative situation."
    },
    "catastrophizing": {
        "explanation": "Exaggerating the importance of insignificant events or mistakes.",
        "reframe": "Ask yourself if the issue will matter in the long term and weigh its actual impact."
    },
    "personalization": {
        "explanation": "Believing that you are the sole cause of every negative event.",
        "reframe": "Understand that not everything is under your control and multiple factors contribute to outcomes."
    },
    "mind_reading": {
        "explanation": "Assuming you know what others are thinking, usually thinking they think negatively of you.",
        "reframe": "Recognize that you cannot read minds and avoid making assumptions without evidence."
    },
    "emotional_reasoning": {
        "explanation": "Believing that your emotions are an accurate reflection of reality.",
        "reframe": "Acknowledge that emotions can sometimes be based on irrational thoughts or biases."
    },
    "should_statements": {
        "explanation": "Having a rigid view of how you or others should behave and getting upset if these rules are not followed.",
        "reframe": "Recognize that people are fallible and that it's more realistic to have preferences rather than rigid expectations."
    },
    "labeling": {
        "explanation": "Assigning global negative traits to yourself and others.",
        "reframe": "Try to view people as complex beings with multiple traits rather than labeling them solely based on specific behaviors."
    },
    "fallacy_of_change": {
        "explanation": "Believing that other people must change in order for you to be happy.",
        "reframe": "Focus on what you can control and change within yourself to improve your well-being."
    }
}

# This can be a list of tips or quotes
daily_tips = [
    "Take deep breaths to help alleviate stress.",
    "Remember, thoughts are not always facts.",
    "Challenge your negative thoughts with evidence.",
    "Remember to be kind to yourself today.",
    "You don't have to be perfect to be amazing.",
    "Don't ruin a good today by thinking about a bad yesterday.",
    "You have the power to change your thoughts, and your thoughts have the power to change your life.",
    "Don't be pushed around by your problems. Be led by your dreams.",
    "Take time to do what makes your soul happy.",
    "Believe in yourself and you will be unstoppable.",
]

# Function to get the tip of the day
def get_daily_tip():
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    random.seed(day_of_year)
    return random.choice(daily_tips)

# For tracking progress
user_progress = {}

def identify_distortion(thought):
    # Logic for identifying distortion

    # Overgeneralization
    if "always" in thought or "never" in thought:
        user_progress["overgeneralization"] = user_progress.get("overgeneralization", 0) + 1
        return "overgeneralization"

    # Black and White Thinking
    if "all or nothing" in thought or "either or" in thought:
        user_progress["black_and_white"] = user_progress.get("black_and_white", 0) + 1
        return "black_and_white"

    # Filtering
    if "only the bad" in thought or "ignoring the good" in thought:
        user_progress["filtering"] = user_progress.get("filtering", 0) + 1
        return "filtering"

    # Catastrophizing
    if "worst-case scenario" in thought or "it's the end" in thought:
        user_progress["catastrophizing"] = user_progress.get("catastrophizing", 0) + 1
        return "catastrophizing"

    # Personalization
    if "my fault" in thought or "because of me" in thought:
        user_progress["personalization"] = user_progress.get("personalization", 0) + 1
        return "personalization"

    # Mind Reading
    if "they think" in thought or "he must think" in thought:
        user_progress["mind_reading"] = user_progress.get("mind_reading", 0) + 1
        return "mind_reading"

    # Emotional Reasoning
    if "I feel it, so it must be true" in thought:
        user_progress["emotional_reasoning"] = user_progress.get("emotional_reasoning", 0) + 1
        return "emotional_reasoning"

    # Should Statements
    if "I should" in thought or "they should" in thought:
        user_progress["should_statements"] = user_progress.get("should_statements", 0) + 1
        return "should_statements"

    # Labeling
    if "I am a" in thought and ("loser" in thought or "failure" in thought):
        user_progress["labeling"] = user_progress.get("labeling", 0) + 1
        return "labeling"

    # Fallacy of Change
    if "they must change" in thought or "if only they" in thought:
        user_progress["fallacy_of_change"] = user_progress.get("fallacy_of_change", 0) + 1
        return "fallacy_of_change"

    # If no distortion is identified
    return None

# Example usage:
thought = "I always fail in everything I try"
distortion = identify_distortion(thought)
if distortion:
    print(f"The thought exhibits {distortion} cognitive distortion.")
else:
    print("No cognitive distortion identified.")

# list of challenges
challenges = [
    "Today, try to write down 3 positive things that happened.",
    "Challenge yourself to avoid using absolute words like 'always' or 'never' today.",
    "Try to do something nice for someone else today, no matter how small.",
    "Today, when you find yourself worrying about something, take 5 deep breaths before continuing.",
    "Challenge yourself to engage in a hobby or activity that makes you happy today.",
    "Take a break from social media for the day and focus on real-life interactions.",
    "Practice mindfulness by spending 10 minutes in quiet meditation or reflection.",
    "Set a goal for yourself and take a small step toward achieving it today.",
    "Challenge negative self-talk by replacing it with positive affirmations.",
    "Express gratitude by writing a thank-you note or telling someone you appreciate them."
]

# Function to get a random challenge
def get_random_challenge():
    return random.choice(challenges)

# Function to get a random challenge
@app.route("/get_challenge", methods=['GET'])
@login_required
def get_challenge():
    return get_random_challenge()

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    thought = None
    result = None
    daily_tip = get_daily_tip()
    random_challenge = get_random_challenge()


    if request.method == 'POST':
        # Get thought from form
        thought = request.form.get('thought')
        # Identify cognitive distortion
        distortion = identify_distortion(thought)
        if distortion:
            result = {
                'distortion': distortion,
                'explanation': cognitive_distortions[distortion]["explanation"],
                'reframe': cognitive_distortions[distortion]["reframe"]
            }
        else:
            result = None

    return render_template('index.html', result=result, thought=thought, daily_tip=daily_tip, random_challenge=random_challenge)

if __name__ == "__main__":
    app.run(debug=True)