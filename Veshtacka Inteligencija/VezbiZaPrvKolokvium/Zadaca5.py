from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    num_of_queens = int(input())
    variables = range(1, num_of_queens + 1)
    domain = [(i, j) for i in range(num_of_queens) for j in range(num_of_queens)]

    for variable in variables:
        problem.addVariable(variable, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for queen1 in variables:
        for queen2 in variables[queen1:]:
            # No two queens are allowed to be on the same line, column or diagonal:
            problem.addConstraint(
                lambda q1, q2: q1[0] != q2[0] and q1[1] != q2[1] and abs(q1[0] - q2[0]) != abs(q1[1] - q2[1]),
                (queen1, queen2))

    # ----------------------------------------------------

    if num_of_queens <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
