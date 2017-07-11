## Overview

A program in Python that solves [KenKen puzzles](https://en.wikipedia.org/wiki/KenKen), by representing the game as a Constraint Satisfaction Problem (CSP).


## Puzzle presentation

### Board
The KenKen board is represented by a square n-by-n grid of cells. The grid may contain between 1 and n boxes (cages) represented by a heavily outlined perimeter. Each cage will contain in superscript: the target digit value for the cage followed by a mathematical operator. 

![kenken](https://github.com/chanioxaris/KenKen-Solver/blob/master/img/kenken.png)

### Constraints

Each valid solution must follow the below rules:

- The only numbers you may write are 1 to N for a NxN size puzzle.
- A number cannot be reapeated within the same row.
- A number cannot be reapeated within the same solumn.
- In a one-cell cage, just write the target number in that cell.
- Each "cage" (region bounded by a heavy border) contains a "target number" and an arithmetic operation. You must fill that cage with numbers that produce the target number, using only the specified arithmetic operation. Numbers may be repeated within a cage, if necessary, as long as they do not repeat within a single row or column.


### Input file

The input format used to describe a puzzle is:


## Algorithms

### Algorithms information

You can select among 5 algorithms to solve a puzzle. These are

### Algorithms comparison

|  Size  |   BT   | BT+MRV |   FC   | FC+MRV |   MAC  | 
| :----: | :----: | :----: | :----: | :----: | :----: |
|   3x3  |   10   |   10   |   9    |   11   |   9    |
|   4x4  |   33   |   24   |   26   |   18   |   19   |  
|   5x5  |   89   |   55   |   42   |   33   |   26   |  
|   6x6  |   947  |   215  |   48   |   68   |   73   |  
|   7x7  |  2600  |   957  |   278  |   320  |   66   |  

## Usage

For windows based systems
`python kenken.py [input file] [algorithm]`


For linux bases systems
`py kenken.py [input file] [algorithm]`

## References

[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)

[aima-python](https://github.com/aimacode/aima-python)
