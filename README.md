# Minesweeper AI Solver

A Python-based AI agent designed to play the classic Minesweeper game using logical reasoning to deduce safe moves, identify mines, and update knowledge dynamically.

## Setup Instructions

### Prerequisites

1. Ensure you have Python 3.7 or later installed on your system.
2. Install all dependencies listed in the `requirements.txt` file.

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Program

1. Start the Minesweeper AI:
   ```bash
   python minesweeper.py
   ```

2. The default board size is 8x8 with 8 mines. You can customize the grid size and number of mines by editing the `Minesweeper()` initialization in `minesweeper.py`:
   ```python
   game = Minesweeper(height=10, width=10, mines=15)
   ```
   Replace `10` and `15` with your desired dimensions and mine count.

## Customization

- **Grid Size**: Modify the `height` and `width` parameters when initializing the `Minesweeper` class.
- **Number of Mines**: Adjust the `mines` parameter in the same initialization.

## Notes

- This project is primarily intended as a demonstration of AI reasoning techniques.
- Ensure that the grid size is sufficiently large compared to the number of mines for optimal gameplay experience.

## Game Play images

<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/start.png" alt="Image 1" width="330">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/play.png" alt="Image 2" width="330">
  <img src="https://github.com/yhnx/minesweeperAIBot/blob/main/img/won.png" alt="Image 3" width="330">
</div>

##
Enjoy exploring the logical prowess of the Minesweeper AI Solver! 🤖
