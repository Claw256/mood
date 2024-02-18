#!/bin/env python3
"""
Fearghal's Mood Recorder (FMR) Version 1.0.1

This program's function is to record and log the mood of a person, offering supportive messages if they are feeling down. It supports input through command line arguments or interactive prompts, ensuring flexibility in how the user chooses to input their current mood.

Author: Fearghal Hayes
Version: 1.0.1
License: MIT License
"""

import argparse
import datetime
import sys


def parse_command_line_args():
    """
    Parses and returns command line arguments.

    This function utilizes argparse to handle command line arguments for the application, specifically looking for a mood value provided with the --mood or -m flag.

    Returns:
        argparse.Namespace: An object containing the parsed command line arguments, notably the mood argument.

    Author: Fearghal Hayes
    Version: 1.0.1
    """
    parser = argparse.ArgumentParser(description="Record and log your mood.")
    parser.add_argument("--mood", "-m", type=int, help="Your mood on a scale from -5 to 5.", required=False)
    return parser.parse_args()


def get_user_mood():
    """
    Prompts the user for their mood and returns it.

    This function asks the user to input their current mood as an integer between -5 and 5, where -5 indicates the worst mood and 5 the best.

    Returns:
        int: The mood rating provided by the user.

    Raises:
        ValueError: If the input is not an integer.

    Author: Fearghal Hayes
    Version: 1.0.1
    """
    try:
        return int(input("How are you feeling today (on a scale from -5 to 5)? "))
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)


def log_mood(mood):
    """
    Logs the user's mood to a file with the current date and time.

    Parameters:
        mood (int): The mood rating from -5 to 5.

    The function writes the mood rating to the 'mood.log' file along with a timestamp of when the mood was recorded.

    Author: Fearghal Hayes
    Version: 1.0.1
    """
    with open("mood.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: Mood = {mood}\n")


def provide_feedback(mood):
    """
    Provides feedback based on the user's mood.

    Parameters:
        mood (int): The mood rating from -5 to 5.

    Depending on the mood rating, the function prints out a supportive or encouraging message to the console.

    Author: Fearghal Hayes
    Version: 1.0.1
    """
    feedback = {
        5: "You're doing great!",
        4: "Looking good!",
        3: "Excellent!",
        2: "You're getting there",
        1: "Good to know",
        0: "Perfectly balanced, as all things should be...",
        -1: "You're going to be ok",
        -2: "There's always darkness before the dawn",
        -3: "Hang in there!",
        -4: "Sorry to hear that :(, things will get better!",
        -5: "Keep your chin up!"
    }
    print(feedback.get(mood, "Thank you for sharing how you feel."))


def main():
    """
    The main entry point of the application.

    This function orchestrates the flow of the program by parsing command line arguments, obtaining the user's mood (either through the command line or interactive input), logging the mood, and providing feedback based on the mood rating.

    Author: Fearghal Hayes
    Version: 1.0.1
    """
    args = parse_command_line_args()
    mood = args.mood if args.mood is not None else get_user_mood()
    if mood < -5 or mood > 5:
        print("Please use the range '-5 to 5'.")
        sys.exit(1)
    log_mood(mood)
    provide_feedback(mood)


if __name__ == "__main__":
    main()
