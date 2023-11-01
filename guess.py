import random
import json

def play_game():
    name = input("Enter your name: ")
    print(f"Welcome {name}! Let's play the python guessing game.")
    print("I am thinking of a number between 0 and 30. You have 10 tries to guess it right.")
    # Random variable generator
    number = random.randint(0, 30)
    tries = 10
    while tries > 0:
        guess = int(input("Guess a number between 0 and 30: "))
        #Loop
        if guess == number:
            print(f"Congratulations {name}! You guessed the number in {11 - tries} tries.")
            save_score(name, 11 - tries)
            break
        else:
            tries -= 1
            if tries == 0:
                print(f"Sorry {name}, you have used up all your tries. The number was {number}.")
                break
            else:
                print(f"Wrong guess. You have {tries} tries left.")

def view_scores():
    try:
        with open("scores.json", "r") as f:
            scores = json.load(f)
        scores.sort(key=lambda x: x["tries"])
        print("High Scores:")
        for i, score in enumerate(scores[:10]):
            print(f"{i+1}. {score['name']} - {score['tries']} tries")
    except FileNotFoundError:
        print("No scores found.")
# Save the scores to the Scores.json file.
def save_score(name, tries):
    try:
        with open("scores.json", "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []
    scores.append({"name": name, "tries": tries})
    scores.sort(key=lambda x: x["tries"])
    with open("scores.json", "w") as f:
        json.dump(scores[:10],  f)

def main():
    while True:
        print("Welcome to the python guessing game, please select an option")
        print("(a) Play\n")
        print("(b) Score\n")
        print("(c) Exit\n")
        choice = input("Enter your choice: ")
        if choice == "a":
            play_game()
        elif choice == "b":
            view_scores()
        elif choice == "c":
            print("Thank you for playing Goodbye!")
            break
        else:
            print("Invalid choice. Please select a, b, or c.")

if __name__ == "__main__":
    main()
