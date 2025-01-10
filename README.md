Mahjong Scorer
==============

Summary
-------
Mahjong Scorer is a Python package designed to manage and score Mahjong games.
It provides functionality to handle player information, game rounds, and scoring, 
making it easier to keep track of the game progress and results.

Features
--------
- **Player Management:** Add and manage players in the game.
- **Game Rounds:** Start and manage game rounds, including tracking the wind of the round.
- **Scoring:** Input and calculate scores for each round, including handling special cases like wind wins.
- **Game:** Information: Display current game information, including player scores and round details.
- **User:** Interaction: Command-line interface for user inputs to control the game flow.

Installation
------------
To install the package, clone the repository:

``git clone https://github.com/KEKEK375/Mahjong-Scorer.git``

Usage
-----
To start the game, either:

Run the ``run.bat``

**OR**

run the main script from the command line:

```bash
cd /path/to/cloned/repository
python -m src
```

Follow the on-screen prompts to manage the game, input scores, and display game information.

Testing
-------
To run the tests, use the following command:

``python -m coverage run -m unittest discover -s tests``

to then get coverage run:

for an xml summary:

``python -m coverage xml``

for a html summary:

``python -m coverage html``

then open ``/htmlcov/index.html``
