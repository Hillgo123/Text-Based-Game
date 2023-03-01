import sys
from termcolor import colored


class initial_opt:
    def __init__(self, name, event_color, actions_color):
        self.name = name
        self.event_color = event_color
        self.actions_color = actions_color


def check_response(response: str, possible_responses: list):
    """Checks if the response is valid."""

    while True:
        response = input(colored('>', opt.actions_color))
        try:
            response = int(response)

        except ValueError:
            pass

        if response == 'q':
            print(colored('Quitting...', opt.actions_color))
            sys.exit()

        if response in possible_responses:
            return response

        else:
            continue


def print_actions(actions: list, possible_responses: list):
    """Prints the actions."""

    for idn, n in enumerate(actions):
        print(colored(f'{idn + 1}:  {n}', opt.actions_color))
        possible_responses.append(idn + 1)


def start():
    start_actions = [f'Play as {opt.name}', 'Options', 'Help', 'Quit']
    p_r = []
    start_r = None
    print(colored('Welcome to the game!', opt.event_color))

    print_actions(start_actions, p_r)
    start_r = check_response(start_r, p_r)

    if start_r == 1:
        event_1()

    elif start_r == 2:
        options()

    elif start_r == 3:
        print(colored('Help is not available yet.', opt.event_color))
        start()

    elif start_r == 4:
        print(colored('Quitting...', opt.actions_color))
        sys.exit()


def options():
    opt_actions = [f'Name: {opt.name}', f'Event Color: {opt.event_color}',
                   f'Actions Color: {opt.actions_color}', 'Back']
    p_r = []
    opt_r = None

    print_actions(opt_actions, p_r)
    opt_r = check_response(opt_r, p_r)

    if opt_r == 1:
        opt.name = input(colored('New name > ', opt.actions_color))
        options()

    elif opt_r == 4:
        start()


def event_1():
    pass


opt = initial_opt('Player', 'white', 'green')

if __name__ == '__main__':
    start()
