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
    

# For tracking progress
user_progress = {}

def identify_distortion(thought):
    # Logic for identifying distortion
    # Example:
    if "always" in thought or "never" in thought:
        return "overgeneralization"
    # Add other conditions
    return None

def main():
    print("Welcome to the Cognitive Distortion Identification Chatbot!")

    user_name = input("What's your name? ")
    if user_name not in user_progress:
        user_progress[user_name] = {}

    while True:
        thought = input("Enter a thought or type 'exit' to quit: ")
        if thought == 'exit':
            break

        distortion = identify_distortion(thought)
        if distortion:
            print("Distortion Identified:", distortion)
            print("Explanation:", cognitive_distortions[distortion]["explanation"])
            print("Reframe Suggestion:", cognitive_distortions[distortion]["reframe"])
            # Track progress
            user_progress[user_name][distortion] = user_progress[user_name].get(distortion, 0) + 1
        else:
            print("No cognitive distortion identified.")

        # Show progress if needed
        print("Progress so far:", user_progress[user_name])

if __name__ == "__main__":
    main()