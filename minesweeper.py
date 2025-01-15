import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.

        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        """
        Simply tells whether the given cell has a mine or not

        """
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.

        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.

        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.

    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.

        """

        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        else:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.

        """
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.

        """
        if cell in self.cells and self.count != 0:
            self.cells.remove(cell)
            newcount = self.count
            self.count = newcount - 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.

        """
        if cell in self.cells and self.count != 0:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player

    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.

        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.

        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        """
        # Mark the cell as a move that has been made
        self.moves_made.add(cell)

        # Mark the cell as safe
        self.mark_safe(cell)

        # Determine neighbors and add a new sentence
        x, y = cell
        neighbors = set()

        for i in range(max(0, x - 1), min(self.height, x + 2)):
            for j in range(max(0, y - 1), min(self.width, y + 2)):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Ignore cells already marked safe or as mines
                if (i, j) in self.safes or (i, j) in self.mines:
                    if (i, j) in self.mines:
                        count -= 1
                    continue

                neighbors.add((i, j))

        # Add the new sentence to knowledge
        if neighbors:
            new_sentence = Sentence(neighbors, count)
            self.knowledge.append(new_sentence)

        # Update knowledge and deduce new information
        self.checkup()

        # Infer new sentences
        self.infer_knowledge()

    def infer_knowledge(self):
        """
        Infers new knowledge from existing sentences.
        Adds new sentences to the knowledge base if one sentence
        is a subset of another.
        """
        new_sentences = []
        for sentence1 in self.knowledge:
            for sentence2 in self.knowledge:

                # identical sentences are skipped
                if sentence1 == sentence2:
                    continue

                # If sentence1 is a subset of sentence2
                if sentence1.cells.issubset(sentence2.cells):
                    inferred_cells = sentence2.cells - sentence1.cells
                    inferred_count = sentence2.count - sentence1.count
                    new_sentence = Sentence(inferred_cells, inferred_count)
                    if (new_sentence not in self.knowledge) and (new_sentence not in new_sentences):
                        new_sentences.append(new_sentence)

        # Add all new sentences to the knowledge base
        self.knowledge.extend(new_sentences)

    def checkup(self):
        """
        Identifying mines or safes based on current knowledge.

        """
        changes_made = True

        # Loop until no further changes are made
        while changes_made:
            changes_made = False

            # Iterate over sentences in the knowledge base
            for sentence in self.knowledge:
                # Iterate over a copy of known safes and known mines
                for cell in sentence.known_safes().copy():
                    if cell not in self.safes:  # Avoid redundant marking
                        self.mark_safe(cell)
                        changes_made = True
                for cell in sentence.known_mines().copy():
                    if cell not in self.mines:  # Avoid redundant marking
                        self.mark_mine(cell)
                        changes_made = True

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe and not already a move
        that has been made.

        """
        # Determine possible safe moves
        possible_moves = self.safes - self.moves_made

        # Return a safe move if available
        if not possible_moves:
            return None

        # Return the first safe move
        return next(iter(possible_moves))

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.

        """
        all = set()
        for i in range(self.width):
            for j in range(self.height):
                all.add((i, j))
        random_moves = (all - self.moves_made) - self.mines

        # Return a random move if available
        if not random_moves:
            return None

        # Return the a random move
        return next(iter(random_moves))
