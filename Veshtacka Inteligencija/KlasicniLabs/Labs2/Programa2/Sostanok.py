from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", (12, 13, 14, 15, 16, 17, 18, 19, 20))

    # ----------------------------------------------------
    simona_slobodni_termini = (13, 14, 16, 19)
    marija_slobodni_termini = (14, 15, 18)
    petar_slobodni_termini = (12, 13, 16, 17, 18, 19)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # Симона како менаџер мора да присуствува на состанокот со најмалку уште една личност:
    problem.addConstraint(
        lambda simona, marija, petar, vreme: simona == 1 and vreme in simona_slobodni_termini and (
                (marija == 1 if vreme in marija_slobodni_termini else marija == 0) and (
                 petar == 1 if vreme in petar_slobodni_termini else petar == 0)),
        ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"]
    )

    # ----------------------------------------------------
    for solution in problem.getSolutions():
        new_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                        'Marija_prisustvo': solution['Marija_prisustvo'],
                        'Petar_prisustvo': solution['Petar_prisustvo'], 'vreme_sostanok': solution['vreme_sostanok']}
        print(new_solution)
