"""

The purpose of this code is to

1. give a quick start to Python programming.
2. show how to use ai tools to generate code based on requirements.
3. have fun learning hex to binary conversion.


It was written by ai (claude) with this prompt:

--- PROMPT ---

write a python script that helps to learn binary to hex conversion.  Do it like this:
* provide a random 4 bit string
* ask user to type in hex notation. If wrong, print correct answer
* quit on "q" input
* make code as simple as possible, without use of functions.
* explain each line with a comment for unexperienced python users

---- END PROMPT ---


"""

# Import random module to generate random numbers
import random

# Print instructions for the user
print("Convert binary (4 bits) to hex. Type 'q' to quit.")

# Start an infinite loop that will run until broken
while True:
    # Generate random number between 0-15 (4 bits) and convert to binary string, remove '0b' prefix and pad with zeros
    binary = format(random.randint(0, 15), "04b")

    # Print the binary number for user to convert
    print(f"\nBinary number: {binary}")

    # Get user input
    answer = input("Enter hex digit (0-9 or a-f): ").lower()

    # Check if user wants to quit
    if answer == "q":
        break

    # Convert the binary string to integer, then to hex string, remove '0x' prefix
    correct = format(int(binary, 2), "x")

    # Check if user's answer is correct and print appropriate message
    if answer == correct:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is: {correct}")

# Print goodbye message when user quits
print("Thanks for practicing!")
