# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic word-guessing game in Python that uses strings, loops, conditionals, and user input. Students will practice managing game state while giving players feedback on their guesses.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the core Hangman game setup, including a predefined list of possible words and logic to choose one at random for each round.

#### Requirements
Completed program should:

- Randomly select a hidden word from a predefined list
- Initialize the game with the correct number of attempts
- Display the hidden word as underscores before any guesses are made
- Prepare the game state needed to track guessed letters


### 🛠️ Gameplay Loop and End Conditions

#### Description
Build the main guessing loop so the player can enter letters, see progress, and finish the game with a win or loss.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the player
- Reveal correctly guessed letters in the word display
- Track incorrect guesses and show how many attempts remain
- End the game when the word is fully guessed or attempts run out
- Display a clear win message when the player guesses the word
- Display a clear lose message when the player uses all attempts
