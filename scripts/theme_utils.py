import re
from random import randint, choice, random
import color_utils

with open('./scripts/default-theme.json') as default_theme_file:
    default_theme = default_theme_file.read()

num_of_colors = len(re.findall('#[0-9a-fA-F]{6}', default_theme))


def generate_random_theme():
    return [[randint(0, 255) for x in range(3)] for _ in range(num_of_colors)]


def generate_theme_text(values=[]):
    index = -1

    def update_value_and_index(x):
        nonlocal index
        if (len(values)):
            index += 1
            rgb = values[index]
        else:
            rgb = [randint(0, 255) for x in range(3)]

        return color_utils.rgb_to_hex(*rgb)

    return re.sub('#[0-9a-fA-F]{6}', update_value_and_index, default_theme)


def theme_from_parents(*parents):
    return [[choice(parents)[color][x] for x in range(3)]
            for color in range(num_of_colors)]


def mutate_theme(theme, likelihood=0.1, amount=1):
    for _ in range(amount):
        if random() < likelihood:
            theme[randint(0, num_of_colors - 1)
                  ][randint(0, 2)] = randint(0, 255)

    return theme


def preview_theme(theme):
    with open('./themes/rl-themer-color-theme.json', 'w') as theme_preview_file:
        theme_preview_file.write(generate_theme_text(theme))
