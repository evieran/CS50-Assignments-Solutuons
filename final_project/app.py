cognitive_distortions = {
    "black_and_white": {
        "explanation": "Seeing things as black-or-white, no middle ground.",
        "reframe": "Try to see the spectrum in between extremes."
    },
    "overgeneralization": {
        "explanation": "Making general interpretations from a single event.",
        "reframe": "Consider that this event might not represent the whole picture."
    },
    # Add other cognitive distortions
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