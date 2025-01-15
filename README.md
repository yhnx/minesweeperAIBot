# Minesweeper AI Solver

A Python-based AI agent designed to play the classic Minesweeper game using logical reasoning to deduce safe moves, identify mines, and update knowledge dynamically.

## Setup Instructions

### Prerequisites

1. Ensure you have Python 3.7 or later installed on your system.
2. Install all dependencies listed in the `requirements.txt` file.

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yhnx/minesweeperAIBot
   cd minesweeperAIBot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Program

1. Start the Minesweeper AI:
   ```bash
   python3 runner.py
   ```

2. The default board size is 8x8 with 8 mines. You can customize the grid size and number of mines by editing the code  in `runner.py`:
   ```python
   HEIGHT = 8
   WIDTH = 8
   MINES = 8
   ```
   Replace `8` with your desired dimensions and mine count.

## Customization

- **Grid Size**: Modify the `HEIGHT` and `WIDTH` parameters.
- **Number of Mines**: Adjust the `MINES` parameter.

## Notes

- This project is primarily intended as a demonstration of knowledge based AI reasoning techniques.
- Ensure that the grid size is sufficiently large compared to the number of mines for optimal gameplay experience.

## Game Play images

<div style="display: flex; flex-wrap: nowrap; justify-content: space-between; align-items: center;">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/start.png" alt="Start" style="width: 30%; max-width: 150px; height: auto;">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/play.png" alt="Play" style="width: 30%; max-width: 150px; height: auto;">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/won.png" alt="Won" style="width: 30%; max-width: 150px; height: auto;">
</div>


##
Enjoy exploring the logical prowess of the Minesweeper AI Solver! 🤖
