## Overview

A program in Python 3.6 that solves [KenKen puzzles](https://en.wikipedia.org/wiki/KenKen), by representing the game as a Constraint Satisfaction Problem (CSP).


## Puzzle representation

### Board
The KenKen board is represented by a square n-by-n grid of cells. The grid may contain between 1 and n boxes (cages) represented by a heavily outlined perimeter. Each cage will contain in superscript: the target digit value for the cage followed by a mathematical operator. 

![kenken](https://github.com/chanioxaris/kenken-solver/blob/master/img/kenken.png)

### Constraints

Each valid solution must follow the below rules:

- The only numbers you may write are 1 to N for a NxN size puzzle.
- A number cannot be reapeated within the same row.
- A number cannot be reapeated within the same solumn.
- In a one-cell cage, just write the target number in that cell.
- Each "cage" (region bounded by a heavy border) contains a "target number" and an arithmetic operation. You must fill that cage with numbers that produce the target number, using only the specified arithmetic operation. Numbers may be repeated within a cage, if necessary, as long as they do not repeat within a single row or column.


### Input file

The input format of text file, used to describe a puzzle is:

```
Puzzle_size
[Square_indexes1] Cage_operator1 Cage_target1
[Square_indexes2] Cage_operator2 Cage_target2
[Square_indexes3] Cage_operator3 Cage_target3
...
[Square_indexesM] Cage_operatorM Cage_targetM
```

<br />

For example, the text representing the above puzzle is:

```
6
[(0,0),(1,0)] add 11
[(0,1),(0,2)] div 2
[(0,3),(1,3)] mult 20
[(0,4),(0,5),(1,5),(2,5)] mult 6
[(1,1),(1,2)] sub 3
[(1,4),(2,4)] div 3
[(2,0),(2,1),(3,0),(3,1)] mult 240
[(2,2),(2,3)] mult 6
[(3,2),(4,2)] mult 6
[(3,3),(4,3),(4,4)] add 7
[(3,4),(3,5)] mult 30
[(4,0),(4,1)] mult 6
[(4,5),(5,5)] add 9
[(5,0),(5,1),(5,2)] add 8
[(5,3),(5,4)] div 2
```


## Algorithms

### Algorithms information

You can select among 5 algorithms to solve a puzzle. These are:
- Backtracking (command line parameter "BT").
- Backtracking with Minimum remaining values (command line parameter "BT+MRV").
- Forward checking (command line parameter "FC").
- Forward checking with Minimum remaining values (command line parameter "FC+MRV").
- Maintaining arc consistency (command line parameter "MAC").


### Algorithms comparison

The below table represents the number of assigments used from each algorithm, to solve different size puzzles.


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
