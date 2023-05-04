from constraint import *

if __name__ == '__main__':
    problem = Problem()

    clenovi_dict = {}
    clenovi_domain = []
    lideri_dict = {}
    lideri_domain = []

    broj_na_clenovi = int(input())
    for i in range(0, broj_na_clenovi):
        line = input().split(" ")
        clenovi_dict[line[1]] = float(line[0])
        clenovi_domain.append(float(line[0]))

    broj_na_lideri = int(input())
    for i in range(0, broj_na_lideri):
        line = input().split(" ")
        lideri_dict[line[1]] = float(line[0])
        lideri_domain.append(float(line[0]))

    # Variables:
    clenovi_variables = [f'Participant {member + 1}' for member in range(0, 5)]
    problem.addVariables(clenovi_variables, clenovi_domain)
    lideri_variables = ["Leader"]
    problem.addVariables(lideri_variables, lideri_domain)

    # Constraints:
    problem.addConstraint(MaxSumConstraint(100))
    problem.addConstraint(AllDifferentConstraint(), clenovi_variables)

    solutions = {}

    for solution in problem.getSolutions():
        max_tezhina = 0
        for value in solution.values():
            max_tezhina += value

        solutions[max_tezhina] = [value for value in solution.values()]

    optimalen_tim = max(solutions.keys())
    cel_tim = solutions[optimalen_tim]
    optimalen_lider = cel_tim[-1]

    print(f'Total score: {round(optimalen_tim, 1)}')

    for key, value in lideri_dict.items():
        if optimalen_lider == value:
            print(f'Team leader: {key}')
            break

    del cel_tim[-1]
    keys = []
    for i in range(len(cel_tim)):
        for key, value in clenovi_dict.items():
            if cel_tim[i] == value:
                keys.append(key)
                break

    keys_new = sorted(keys, reverse=True)
    for i in range(0, 5):
        print(f'Participant {i + 1}: {keys_new[i]}')
