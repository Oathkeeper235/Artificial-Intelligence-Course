from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    solver = input()

    if solver == "BacktrackingSolver":
        problem = Problem(BacktrackingSolver())
    elif solver == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())
    elif solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())

    domain = range(1, 10)  # numbers from 1 to 9

    variables = [i for i in range(0, 81)]  # The sudoku game area is 9x9 or 81 fields
    for variable in variables:
        problem.addVariable(variable, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # rows and columns constraint:
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [i * 9 + num for num in range(9)])
        problem.addConstraint(AllDifferentConstraint(), [i + 9 * num for num in range(9)])

    # constraint for every 3 x 3 square:
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(),
                                  [i * 9 + j for i in range(row, row + 3) for j in range(col, col + 3)])

    # ----------------------------------------------------

    print(problem.getSolution())
