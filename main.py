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
        pass


def check_response(response: str, possible_responses: list):
    """Checks if the response is valid."""

    while True:
        response = input(colored('> ', opt.actions_color))
        try:
            response = int(response)

        except ValueError:
            pass

        if response == 'q':
            print(colored('Quitting...', opt.actions_color))
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
    print(colored('Welcome to the game!', opt.event_color))

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
        print(colored('Quitting...', opt.actions_color))
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
    pass


opt = store_options('Player', 'white', 'green')
responses = store_responses()

if __name__ == '__main__':
    clear_console()
    start()
