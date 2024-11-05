# type: ignore
import random
from enum import Enum, auto
from time import time


# ANSI escape codes for colors
class Colors:
    """Color codes for terminal output"""

    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"


class Command(Enum):
    """Enum for different user commands"""

    QUIT = auto()
    HELP = auto()
    STATS = auto()
    ANSWER = auto()


def generate_question():
    """Generate a random 4-bit binary number and its corresponding hex value"""
    binary = format(random.randint(0, 15), "04b")
    hex_value = format(int(binary, 2), "x")
    return binary, hex_value


def show_cheat_sheet():
    """Print a cheat sheet of binary to hex conversions"""
    print("\nBinary to Hex Cheat Sheet:")
    print("-" * 20)
    for i in range(16):
        binary = format(i, "04b")
        hex_value = format(i, "x")
        print(f"{binary} -> {hex_value}")
    print("-" * 20)


def show_stats(stats):
    """Display current statistics"""
    print("\nCurrent Statistics:")
    print("-" * 20)

    if stats["total"] > 0:
        success_rate = (stats["correct"] / stats["total"]) * 100
        avg_time = stats["total_time"] / stats["total"]

        print(f"Total attempts: {stats['total']}")
        print(f"Correct answers: {stats['correct']}")
        print(f"Success rate: {success_rate:.1f}%")
        print(f"Average response time: {avg_time:.2f} seconds")
        print(f"Current streak: {stats['current_streak']}")
        print(f"Best streak: {stats['best_streak']}")
    else:
        print("No attempts yet!")
    print("-" * 20)


def process_user_input(binary):
    """
    Process user input and determine the command type
    Returns: tuple (Command, user_input)
    """
    print(f"\nBinary number: {binary}")
    print("Commands: 'q' to quit, 'h' for help, 's' for stats")

    start_time = time()
    user_input = input("Enter hex digit (0-9 or a-f): ").lower()
    response_time = time() - start_time

    match user_input:
        case "q":
            return Command.QUIT, user_input, response_time
        case "h":
            return Command.HELP, user_input, response_time
        case "s":
            return Command.STATS, user_input, response_time
        case _:
            return Command.ANSWER, user_input, response_time


def handle_answer(user_answer, correct_answer, stats, response_time):
    """Handle user's answer and update statistics"""
    stats["total"] += 1
    stats["total_time"] += response_time

    is_correct = user_answer == correct_answer

    if is_correct:
        print(
            f"{Colors.GREEN}Correct!{Colors.RESET} (Response time: {response_time:.2f}s)"
        )
        stats["correct"] += 1
        stats["current_streak"] += 1
        stats["best_streak"] = max(stats["best_streak"], stats["current_streak"])
    else:
        print(
            f"{Colors.RED}Wrong! The correct answer is: {correct_answer}{Colors.RESET}"
        )
        print(f"Response time: {response_time:.2f}s")
        stats["current_streak"] = 0


def show_final_stats(stats):
    """Display final statistics with detailed information"""
    if stats["total"] > 0:
        print("\nFinal Statistics:")
        print("-" * 20)
        success_rate = (stats["correct"] / stats["total"]) * 100
        avg_time = stats["total_time"] / stats["total"]

        print(f"Total questions attempted: {stats['total']}")
        print(f"Correct answers: {stats['correct']}")
        print(f"Final success rate: {success_rate:.1f}%")
        print(f"Best streak: {stats['best_streak']}")
        print(f"Average response time: {avg_time:.2f} seconds")
        print("-" * 20)


def practice_session():
    """Run the main practice session loop"""
    print("Convert binary (4 bits) to hex.")
    print("Commands: 'q' to quit, 'h' for help, 's' for stats")

    # Initialize statistics dictionary
    stats = {
        "total": 0,
        "correct": 0,
        "total_time": 0,
        "current_streak": 0,
        "best_streak": 0,
    }

    while True:
        binary, correct_hex = generate_question()
        command, user_input, response_time = process_user_input(binary)

        match command:
            case Command.QUIT:
                break
            case Command.HELP:
                show_cheat_sheet()
            case Command.STATS:
                show_stats(stats)
            case Command.ANSWER:
                handle_answer(user_input, correct_hex, stats, response_time)
            case _:
                print("Invalid command!")

    show_final_stats(stats)
    print("Thanks for practicing!")


def main():
    """Main program entry point"""
    try:
        practice_session()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
