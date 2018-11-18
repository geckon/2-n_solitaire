<pre>
  ___  _ __     _____       _ _ _        _
 |__ \| '_ \   / ____|     | (_) |      (_)
    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
  / /_         ____) | (_) | | | || (_| | | | |  __/
 |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|

</pre>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37d712df43e44d6487bb35e015c27c47)](https://app.codacy.com/app/geckon/2-n_solitaire?utm_source=github.com&utm_medium=referral&utm_content=geckon/2-n_solitaire&utm_campaign=Badge_Grade_Dashboard)
[![Updates](https://pyup.io/repos/github/geckon/2-n_solitaire/shield.svg)](https://pyup.io/repos/github/geckon/2-n_solitaire/)

2<sup>n</sup> Solitaire is a simple game inspired by 2048 Solitaire (but more
generic) which is inspired by 2048 (but instead of tiles in a grid you collect
cards here). I find the game fun and satisfying and thus I decided to try and
implement it using Pygame. Here we are.

The goal of the game is to stack an endless row of cards into limited-size
columns. Each time you stack two cards of the same value one on the other,
the two cards are replaced by one of double the value and your score grows.
Cards with the maximum value (configurable, 2048 by default) will disappear.
The game ends once all the columns are full and so no more cards can be played.

### Controls

![Screenshot](docs/screenshot.png)

This is what the game looks like. At the top you can see your current score,
below that is the main board where the cards are stacked. In the bottom part you
can see two next cards that will come to the game. You can use `1`, `2`, `3` and
`4` keys to place the next upcoming card to the respective column. That's it.
Simple, eh?

### Current state

The game works but doesn't do anything fancy or look fancy yet.

### Future plans

-   High score recording
-   Special cards?
-   Limited swapping *next cards*?
-   Limited discarding *next cards*?
-   Saving game state on exit?
-   Better *graphics*?
-   Mouse support?

See/add issues if interested in anything particular.
