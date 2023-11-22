import random
from random import choice, sample

from exercices_list import all_exercises_list

modificators = [
    'flippers',
    'paddles',
    'pipe',
]

dist_for_tech = [100, 200]
swimming_style = all_exercises_list[1]  # Вот тут указывай стиль


def main(exercise_list, distance=0):
    while True:
        num_1 = random.randint(1, len(exercise_list) - 1)
        num_mods = choice(range(len(modificators) + 1))
        dist = choice(dist_for_tech)
        # print(f'{distance} до начисления')
        distance += dist
        mods = sample(modificators, k=num_mods)
        exercise = exercise_list.pop(num_1)

        print(f'{dist} | {exercise} | {mods}')
        # print(f'{distance} после начисления')
        if distance > 1000:
            print(f'\nИтого {distance}м')
            break


if __name__ == "__main__":
    main(swimming_style)
