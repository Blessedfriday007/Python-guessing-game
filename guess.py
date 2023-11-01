import random
import shelve

# Open the file containing the high scores
with shelve.open('scores') as db:
    # Retrieve the high scores from the database
    scores = db.get('scores', [])

    # Add the new score to the list of high scores
    scores.append(scores)

    
    # Limit the high scoreboard list to 10 entries
    scores = scores[:10]

    # Save the updated list of high scores to the database
    db['scores'] = scores

def play_game():
    name = input("Enter your name: ")
    print("Hello, " + name + "! Welcome to the python guessing game.")
    print("I am thinking of a number between 0 and 30. You have 10 tries to guess it right.")
    # random variable generator
    number = random.randint(0, 30)
    tries = 0
    while tries < 10:
        guess = int(input("Guess the number: "))
        tries += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high ")
        else:
            print("Congratulations! You guessed the number in " + str(tries) + " tries.")
            return name, tries
    print("Sorry, you ran out of tries. The number was " + str(number) + ".")
    return name, -1

def view_scores(scores):
    print("High Scores:") 
    for score in scores:
        if score[1] == -1:
            print(score[0] + ": Failed")
        else:
            print(score[0] + ": " + str(score[1]) + " tries")

def main():
    scores = []
    while True:
        # User A is greeted with a menu, asking to choose an action
        print("Welcome to the python guessing game, please select an option")
        print("(a) Play\n")
        print("(b) View High Scores\n")
        print("(c) Exit\n")
        
        choice = input("Enter your choice: ")
        if choice == "a":
            score = play_game()
            
            scores.append(score)  
        elif choice == "b":
            view_scores(scores[-10:])
        elif choice == "c":
            print("Thank you for playing Goodbye!...")
            break
        else:
            print("Invalid choice. Please select a, b, or c.")

if __name__ == "__main__":
    main()

# Optional goals not perfectly implemented ......




