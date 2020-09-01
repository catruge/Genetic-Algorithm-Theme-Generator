from random import random

import theme_utils
import input_utils


def pick_theme(themes):
    sum_of_ratings = sum([theme['rating'] for theme in themes])
    random_number = random() * sum_of_ratings
    chosen_theme_number = 0
    while themes[chosen_theme_number]['rating'] < random_number:
        random_number -= themes[chosen_theme_number]['rating']
        chosen_theme_number += 1

    return themes[chosen_theme_number]


batch = [{'theme': theme_utils.generate_random_theme()} for _ in range(5)]

while True:
    print('\nStarting round...\n')
    for theme in batch:
        theme_utils.preview_theme(theme['theme'])
        theme['rating'] = float(input_utils.get_input(
            'Please rate theme: ', lambda x: input_utils.is_int(x) and int(x) >= 0))

    new_batch = []
    for theme in batch:
        new_batch.append({'theme': theme_utils.mutate_theme(
            theme_utils.theme_from_parents(*[pick_theme(batch)['theme'] for _ in range(2)]))})

    batch = new_batch
