# Tetris Engine

### Running the Engine

The engine reads moves from standard input and outputs the resulting board height after each sequence:

```bash
python tetris.py < input.txt > output.txt
```

### Input Format

The engine accepts input in the following format:

```
I0,I4,Q8
T1,Z3,I4
Q0,I2,I6,I0,I6,I6,Q2,Q4
```

Each line represents a separate game sequence. The engine will output the final height of the board after each sequence.

## Board Details

- Width: 10 columns (0-9)
- Height: 100 rows
- Empty spaces are represented by 0
- Filled spaces are represented by 1
