import pathlib
import sys
import random


ex_unit_list = [["Summer Fjorm", "Plumeria", "Ascended Tiki"], ["Fjorm", "Azura", "Khadein Soren", "Fallen Ninian"],["Anna", "Bridal Anna"],["Jeorge", "Eir", "Ascended Celica"]]


def team_randomizer(unit_list):
    randomized_team = []

    for color in unit_list:
        rand_unit = random.choice(color)
        randomized_team.append(rand_unit)

    print(randomized_team)
    print("Your randomized team is...")
    for unit in range(len(randomized_team)):
        print(randomized_team[unit])

print(team_randomizer(ex_unit_list))
