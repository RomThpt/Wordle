# 🎉 Wordle Choice Game 🎉

A customizable Wordle-inspired game in Python with a twist! Choose your word length, switch to dark mode, play in Pokémon theme, and customize your settings. Built with `guizero`, this game is simple yet endlessly entertaining! 

---

## 📑 Table of Contents
- ✨ [Features](#features)
- 📋 [Requirements](#requirements)
- 🛠️ [Installation](#installation)
- 🎮 [How to Play](#how-to-play)
- 🔍 [Gameplay Modes](#gameplay-modes)
- 📂 [Code Overview](#code-overview)
- 📜 [License](#license)

---

## ✨ Features

- 🔢 **Customizable Word Length**: Pick any word length between 2 and 5 letters.
- 🌑 **Dark Mode**: Switch between light and dark themes for a more comfortable experience.
- 🎮 **Two Game Modes**:
  - 🕹️ Classic mode
  - 🐉 Pokémon-themed mode
- ⚙️ **Settings Window**: Customize background, text, and button colors to your liking.
- 🟩🟨 **Word Verification**: Get instant feedback with color-coded hints.
- 🧹 **Scraping Feature**: Automatically fetches French words (2-5 letters) from an online source.

---

## 📋 Requirements

- **Python 3.6+**
- `guizero` for GUI
- `requests` for web scraping
- `BeautifulSoup` for parsing HTML

Install these with:
```bash
pip install guizero requests beautifulsoup4 unidecode
```
🛠️ Installation

1.	Clone the repository:
```console
git clone https://github.com/yourusername/wordle-choice-game.git
cd wordle-choice-game
```
2. Run the game
```
python main.py
```
## 🎮 How to Play

1. Choose Word Length: Pick your desired word length from 2 to 5 letters.
2.	Make a Guess: Use the on-screen keyboard to type in your guess, then hit Enter to submit.
3.	Check Your Colors:
	-	🟩 Green: Correct letter in the correct spot!
	-	🟨 Yellow: Correct letter, wrong spot!
4.	Win or Try Again: You have five attempts per word—good luck!

## 🔍 Gameplay Modes

- Classic Mode: Regular Wordle gameplay.
- Pokémon Mode: Pokémon-themed visuals and styles for a fun twist!

## 📂 Code Overview

-	main.py: Houses all primary functions for the GUI, word checks, and word scraping.
-	Key Functions:
-	first_window: Sets up the main menu for choosing word length and mode.
-	parameter: Opens a customization window for background and color themes.
-	set_game: Main game loop; selects the word, checks guesses, and handles feedback.
-	scrap: Scrapes French words from [https://listesdemots.net](https://www.listesdemots.net/) based on word length.
-	Dependencies:
-	guizero: GUI elements like windows and buttons.
-	requests & BeautifulSoup: Scrapes words for gameplay.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

# 🎉 Enjoy your word-guessing adventure! 🎉
