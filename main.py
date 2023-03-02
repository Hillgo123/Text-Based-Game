import sys
import os
from termcolor import colored


class store_options:
    """Store options."""

    def __init__(self, name: str, event_color: str, actions_color: str):
        self.name = name
        self.event_color = event_color
        self.actions_color = actions_color
        self.all_colors = ['light_grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
                           'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan']


class store_responses:
    """Store responses and handle consequences."""

    def __init__(self):
        self.e_1 = None
        self.e_2 = None
        self.e_3 = None
        self.e_4 = None
        self.e_5 = None
        self.e_6 = None
        self.e_7 = None


def check_response(response: str, possible_responses: list):
    """Checks if the response is valid."""

    while True:
        response = input(colored('> ', opt.actions_color))
        try:
            response = int(response)

        except ValueError:
            pass

        if response == 'q':
            print(colored('Quitting...', opt.event_color))
            sys.exit()

        if response == 'h':
            print(colored('Help is not available yet.', opt.event_color))
            continue

        if response in possible_responses:
            return response

        else:
            continue


def print_actions(actions: list, possible_responses: list):
    """Prints the actions."""

    for id_action, action in enumerate(actions):
        print(colored(f'{id_action + 1}:  {action}', opt.actions_color))
        possible_responses.append(id_action + 1)


def clear_console():
    """Clears the console."""

    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    """Start menu."""

    start_actions = [f'Play as {opt.name}', 'Options', 'Help', 'Quit']
    p_r = []
    r = None
    print(colored('Welcome to the Survival of the Weirdest!', opt.event_color))

    print_actions(start_actions, p_r)
    r = check_response(r, p_r)

    if r == 1:
        clear_console()
        event_1()

    elif r == 2:
        clear_console()
        options()

    elif r == 3:
        clear_console()
        print(colored('Help is not available yet.', opt.event_color))
        start()

    elif r == 4:
        print(colored('Quitting...', opt.event_color))
        sys.exit()


def options():
    """Options menu."""

    opt_actions = [f'Name: {opt.name}', f'Event Color: {opt.event_color}',
                   f'Actions Color: {opt.actions_color}', 'Back']
    p_r = []
    r = None

    print_actions(opt_actions, p_r)
    r = check_response(r, p_r)

    if r == 1:
        opt.name = input(colored('New name > ', opt.actions_color))
        clear_console()
        options()

    elif r == 2:
        print(
            colored('Colors: ', opt.event_color) + colored(f'{", ".join(opt.all_colors)}', opt.actions_color))

        new_color = ''
        print(
            colored('New event color:', opt.event_color))

        opt.event_color = check_response(new_color, opt.all_colors)

        clear_console()
        options()

    elif r == 3:
        print(
            colored('Colors: ', opt.event_color) + colored(f'{", ".join(opt.all_colors)}', opt.actions_color))

        new_color = ''
        print(
            colored('New actions color:', opt.event_color))

        opt.actions_color = check_response(new_color, opt.all_colors)

        clear_console()
        options()

    elif r == 4:
        clear_console()
        start()


def event_1():
    print(
        colored('Welcome to "Survival of the Weirdest"! You wake up on a deserted beach with nothing but the clothes on your back and a few scraps of debris washed up on shore. You can see that the island is covered in a thick jungle, and you can hear strange noises coming from within.', opt.event_color))

    p_r = []
    r = None

    e_actions = ['Explore the jungle', 'Build a shelter on the beach',
                 'Collect food and water from the surrounding area']

    print_actions(e_actions, p_r)
    responses.e_1 = check_response(r, p_r)

    if responses.e_1 == 1:
        clear_console()
        event_2()

    elif responses.e_1 == 2:
        clear_console()
        event_5()

    elif responses.e_1 == 3:
        clear_console()
        event_8()


def event_2():
    print(
        colored('As you make your way into the jungle, you start to notice some strange things. The trees seem to have faces, and the bushes are shaped like animals. You hear giggling coming from somewhere ahead.', opt.event_color))

    p_r = []
    r = None

    e_actions = ['Investigate the giggling sounds.',
                 'Avoid the giggling and keep moving forward.',
                 'Go back to the beach.', ]

    print_actions(e_actions, p_r)
    responses.e_2 = check_response(r, p_r)

    if responses.e_2 == 1:
        clear_console()
        event_3()

    elif responses.e_2 == 2:
        clear_console()
        event_4()

    elif responses.e_2 == 3:
        clear_console()
        event_1()


def event_3():
    clear_console()

    print(
        colored('You head towards the giggling, curious about who or what is making the noise. As you get closer, you see a group of monkeys playing with a coconut. They stop when they see you and start to screech loudly. Suddenly, they all charge towards you, baring their sharp teeth and claws.', opt.event_color))

    print(colored('Game Over! The monkeys were too aggressive and you were unable to defend yourself', opt.event_color))


def event_4():
    clear_console()

    print(colored('As you approach the treehouse, you suddenly feel yourself falling through a hidden trapdoor in the ground. You land with a thud on a hard surface, and realize that youre in some kind of underground chamber. The door above you slams shut, leaving you in complete darkness.You hear a voice coming from somewhere in the chamber. "Welcome to your new home," the voice says.'))
    print(colored('"Youre never leaving." Game over.', opt.event_color))


def event_5():
    clear_console()

    p_r = []
    r = None

    e_actions = ['Investigate the rustling in the bushes',
                 'Continue building the shelter',
                 'Look for more resources on the beach.', ]

    print(colored('You begin gathering driftwood, palm fronds, and any other materials you can find to build your shelter. As you work, you hear rustling in the nearby bushes.'))

    print_actions(e_actions, p_r)
    responses.e_5 = check_response(r, p_r)

    if responses.e_5 == 1:
        clear_console()
        event_6()

    elif responses.e_5 == 2:
        clear_console()
        event_7()

    elif responses.e_5 == 3:
        clear_console()
        event_8()


def event_6():
    clear_console()

    print(colored('You cautiously approach the rustling in the bushes and find a group of aggressive monkeys gathered around a pile of fruit. They start hurling coconuts and sticks at you, forcing you to retreat back to your shelter. Unfortunately, the monkeys follow you and continue to attack. You try to defend yourself, but the monkeys are too many and too strong. You are unable to fend them off and are eventually overcome. Your journey on the island ends here.', opt.event_color))
    print(colored('Game over.', opt.event_color))


def event_7():
    clear_console()

    print(colored('Now you have a shelter'))

    p_r = []
    r = None

    e_actions = ['Investigate the rustling in the bushes',
                 'Look for more resources on the beach.', ]

    print_actions(e_actions, p_r)
    responses.e_7 = check_response(r, p_r)

    if responses.e_7 == 1:
        clear_console()
        event_6()

    elif responses.e_7 == 2:
        clear_console()
        event_8()


def event_8():
    clear_console()

    print(colored('As you search for more resources on the beach, you come across a talking coconut with a monocle and a top hat.', opt.event_color))
    print(colored('The coconut says, "Good day, old chap! What seems to be the problem?"', opt.event_color))

    p_r = []
    r = None

    e_actions = ['Ignore the coconut and keep searching for resources',
                 'Talk to the coconut and ask for help',
                 'Take a bite out of the coconut, thinking it will solve your hunger problem.']

    print_actions(e_actions, p_r)
    responses.e_7 = check_response(r, p_r)

    if responses.e_7 == 1:
        clear_console()

    elif responses.e_7 == 2:
        clear_console()

    elif responses.e_7 == 3:
        clear_console()


opt = store_options('Player', 'white', 'green')
responses = store_responses()

if __name__ == '__main__':
    clear_console()
    start()
