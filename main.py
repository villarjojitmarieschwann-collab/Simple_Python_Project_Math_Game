# A Simple Python Math Game with Three Difficulty Levels
# Made to practice math and learn Python :)

import random  # used to get random numbers

score = 0  # total score for all levels

# this function runs one level of the game
def play_level(level):
    global score  # so the score adds up

    print("\nStarting level", level)

    for i in range(5):  # ask 5 questions per level

        if level == 1:
            # easy level (addition)
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            answer = a + b
            user = int(input(f"{a} + {b} = "))

        elif level == 2:
            # medium level (subtraction)
            a = random.randint(10, 50)
            b = random.randint(1, 20)
            answer = a - b
            user = int(input(f"{a} - {b} = "))

        elif level == 3:
            # hard level (multiplication)
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            answer = a * b
            user = int(input(f"{a} * {b} = "))

        # checks the answer
        if user == answer:
            print("Correct!")
            score += 1  # add score
        else:
            print("Wrong! The answer is", answer)


# welcome message
print("Welcome to the Math Game!")
print("Choose a level to start:")
print("1 - Easy")
print("2 - Medium")
print("3 - Hard")

level = int(input("Enter level (1-3): "))

# play the first chosen level
play_level(level)

# after finishing a level
while True:
    print("\nGreat job!")
    print("Your current score is:", score)
    choice = input("Would you like to try another level? (yes/no): ")

    if choice == "yes":
        print("\nChoose another level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        level = int(input("Enter level (1-3): "))
        play_level(level)

    else:
        # ending message
        print("\nThanks for playing!")
        print("Your final score is:", score)
        print("Game Over :)")
        break
