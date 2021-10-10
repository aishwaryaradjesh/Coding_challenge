# Coding_challenge

Contents:
  1. main.py 
  2. input.txt

main.py is the python program to evaluate a set of equations, each specified on separate lines. 
 
The main.py will take a text file 'input.txt' as input.
The input.txt should be placed in the same path as main.py
The input.txt should contain a set of equations, each specified on separate lines.

Sample test cases have been provided in the input.txt

## Comments
This equation solver only solves equations with '+' operator.

Lines in the input file that do not follow the expression format LHS = RHS will not be executed.
  
All numbers in the RHS is assumed to be integers as presented in the problem statements. If the RHS contains float values, it will be converted to integer.
  
  For example: 
  
    random = 2.05 will result as random = 2
  
## Example test input
  
  ```
  offset = 4 + random + 1

  g
  **

  = 6
  ==
  *=
  a*=
  location = 1 + origin + offset
  origin = 3         + 5
  random = 2.05
  ```
  
## Example Output
  
  ```
  location  =  16
  origin  =  8
  offset  =  7
  random  =  2
  ```

