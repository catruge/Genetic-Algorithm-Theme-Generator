def get_input(prompt, condition):
    while True:
        user_input = input(prompt)
        if condition(user_input):
            return user_input
        print('Sorry. I didn\'t understand.')


def is_int(x):
    try:
        int(x)
        return True
    except:
        return False
