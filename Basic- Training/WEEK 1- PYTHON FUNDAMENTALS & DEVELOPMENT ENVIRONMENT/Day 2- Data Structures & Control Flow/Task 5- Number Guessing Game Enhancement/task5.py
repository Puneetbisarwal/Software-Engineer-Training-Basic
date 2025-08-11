import random
import json
import os

# ===== High Score Persistence =====
HIGH_SCORE_FILE = "high_scores.json"

def load_high_scores():
    """Load high scores from JSON file."""
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    return {"Easy": None, "Medium": None, "Hard": None}

def save_high_scores(scores):
    """Save high scores to JSON file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(scores, file, indent=4)

# ===== Game Logic =====
def select_difficulty():
    """Allow player to choose difficulty and return range."""
    print("\nChoose difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            return "Easy", 1, 10
        elif choice == "2":
            return "Medium", 1, 50
        elif choice == "3":
            return "Hard", 1, 100
        else:
            print("❌ Invalid choice. Try again.")

def calculate_score(attempts, max_range):
    """Score formula: higher score for fewer attempts & harder range."""
    base_score = max_range * 10
    return max(10, base_score - (attempts - 1) * (max_range // 2))

def play_game():
    scores = load_high_scores()
    difficulty, low, high = select_difficulty()

    number_to_guess = random.randint(low, high)
    attempts = 0

    print(f"\n🎮 I have picked a number between {low} and {high}. Try to guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low!")
            elif guess > number_to_guess:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                score = calculate_score(attempts, high)
                print(f"🏆 Your score: {score}")

                # High score check
                if scores[difficulty] is None or score > scores[difficulty]:
                    scores[difficulty] = score
                    print("🎯 New high score!")
                else:
                    print(f"Current high score for {difficulty}: {scores[difficulty]}")

                save_high_scores(scores)
                break
        except ValueError:
            print("❌ Please enter a valid number.")

# ===== Main Menu =====
def main():
    while True:
        print("\n=== Number Guessing Game ===")
        print("1. Play Game")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            scores = load_high_scores()
            print("\n📜 High Scores:")
            for level, score in scores.items():
                print(f"{level}: {score if score is not None else 'No score yet'}")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
