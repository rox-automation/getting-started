#!/usr/local/bin/python3

from dataclasses import dataclass
from enum import Enum, auto
from time import time
from typing import Final
import random


class Command(Enum):
    """Available user commands."""
    QUIT = auto()
    HELP = auto()
    STATS = auto()
    ANSWER = auto()


@dataclass
class GameStats:
    """Statistics for the practice session."""
    total: int = 0
    correct: int = 0
    total_time: float = 0.0
    current_streak: int = 0
    best_streak: int = 0

    @property
    def success_rate(self) -> float:
        """Calculate the success rate as a percentage."""
        return (self.correct / self.total * 100) if self.total > 0 else 0.0

    @property
    def average_time(self) -> float:
        """Calculate the average response time in seconds."""
        return self.total_time / self.total if self.total > 0 else 0.0

    def show_stats(self) -> None:
        """Display current game statistics."""
        print("\nCurrent Statistics:")
        print("-" * 20)

        if self.total > 0:
            print(f"Total attempts: {self.total}")
            print(f"Correct answers: {self.correct}")
            print(f"Success rate: {self.success_rate:.1f}%")
            print(f"Average response time: {self.average_time:.2f} seconds")
            print(f"Current streak: {self.current_streak}")
            print(f"Best streak: {self.best_streak}")
        else:
            print("No attempts yet!")
        print("-" * 20)

    def show_final_stats(self) -> None:
        """Display final game statistics."""
        if self.total > 0:
            print("\nFinal Statistics:")
            print("-" * 20)
            print(f"Total questions attempted: {self.total}")
            print(f"Correct answers: {self.correct}")
            print(f"Final success rate: {self.success_rate:.1f}%")
            print(f"Best streak: {self.best_streak}")
            print(f"Average response time: {self.average_time:.2f} seconds")
            print("-" * 20)


class BinaryHexGame:
    """Main game class handling the practice session logic."""

    GREEN: Final[str] = "\033[92m"
    RED: Final[str] = "\033[91m"
    RESET: Final[str] = "\033[0m"

    def __init__(self) -> None:
        self.stats = GameStats()

    def show_cheat_sheet(self) -> None:
        """Display a conversion reference sheet."""
        print("\nBinary to Hex Cheat Sheet:")
        print("-" * 20)
        for i in range(16):
            binary = format(i, "04b")
            hex_value = format(i, "x")
            print(f"{binary} -> {hex_value}")
        print("-" * 20)

    def get_user_input(self, binary: str) -> tuple[Command, str, float]:
        """Process user input and return command type with timing."""
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

    def handle_answer(self, user_answer: str, correct_answer: str, response_time: float) -> None:
        """Process user's answer and update statistics."""
        self.stats.total += 1
        self.stats.total_time += response_time

        if user_answer == correct_answer:
            print(
                f"{self.GREEN}Correct!{self.RESET} "
                f"(Response time: {response_time:.2f}s)"
            )
            self.stats.correct += 1
            self.stats.current_streak += 1
            self.stats.best_streak = max(self.stats.best_streak, self.stats.current_streak)
        else:
            print(
                f"{self.RED}Wrong! The correct answer is: "
                f"{correct_answer}{self.RESET}"
            )
            print(f"Response time: {response_time:.2f}s")
            self.stats.current_streak = 0

    def run(self) -> None:
        """Run the main game loop."""
        print("Convert binary (4 bits) to hex.")
        print("Commands: 'q' to quit, 'h' for help, 's' for stats")

        while True:
            question = self.generate_question()
            command, user_input, response_time = self.get_user_input(question)

            match command:
                case Command.QUIT:
                    break
                case Command.HELP:
                    self.show_cheat_sheet()
                case Command.STATS:
                    self.stats.show_stats()
                case Command.ANSWER:
                    self.handle_answer(user_input, self.get_correct_answer(question), response_time)

        self.stats.show_final_stats()
        print("Thanks for practicing!")

    def generate_question(self) -> str:
        """Generate a binary question."""
        return format(random.randint(0, 15), "04b")

    def get_correct_answer(self, binary: str) -> str:
        """Get the correct hex answer for a binary question."""
        return format(int(binary, 2), "x")


def main() -> None:
    """Main program entry point with error handling."""
    try:
        game = BinaryHexGame()
        game.run()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
