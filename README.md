## Overview

A program in Python that solves [KenKen puzzles](https://en.wikipedia.org/wiki/KenKen), by representing the game as a Constraint Satisfaction Problem (CSP). You can select among 5 algorithms to solve each puzzle.


## Puzzle presentation

### Board

### Constraints

### Input file


## Algorithms comparison

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
