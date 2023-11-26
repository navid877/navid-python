import random

rend = random.randrange(1, 51)  # To include 50 in the range
# print(rend)

while True:
    ans_input = int(input("Guess the number from 1 to 50 (or enter 0 to quit): "))
    
    if ans_input == 0:
        print("Quitting the game. The number was:", rend)
        break
    
    if ans_input > 50:
        print("Please enter a number less than or equal to 50.")
        continue
    
    if ans_input == rend:
        print("congratulation!!", ans_input, "is the correct answer!")
        break
    elif ans_input > rend:
        print("Your guess is too high! Try a lower number than", ans_input)
    elif ans_input < rend:
        print("Your guess is too low! Try a higher number than", ans_input)
