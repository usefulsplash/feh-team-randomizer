import pathlib
import sys
import random


def parse(unit_list):
    data = [line.split("\n") for line in unit_list.split("\n\n")]
    return data

def team_randomizer(unit_list):
    randomized_team = []

    for color in unit_list:
        rand_unit = random.choice(color)
        randomized_team.append(rand_unit)
    
    return randomized_team

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        user_unit_list = pathlib.Path(path).read_text().strip()
        data = parse(user_unit_list)
        randomized_team = team_randomizer(data)
        print("\n".join(str(unit) for unit in randomized_team))
