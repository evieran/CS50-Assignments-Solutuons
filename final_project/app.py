import datetime
import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

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

@app.route("/", methods=['GET', 'POST'])
def index():
    thought = None
    result = None
    daily_tip = get_daily_tip()

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

    return render_template('index.html', result=result, thought=thought, daily_tip=daily_tip)

if __name__ == "__main__":
    app.run(debug=True)