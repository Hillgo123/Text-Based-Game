import sys
import os
from termcolor import colored


class store_options:
    """Store options."""

    def __init__(self, name: str, event_color: str, actions_color: str):
        self.name = name
        self.event_color = event_color
        self.actions_color = actions_color
        self.all_colors = ['red', 'green', 'yellow',
                           'blue', 'magenta', 'cyan', 'white']


class store_responses:
    """Store responses and handle consequences."""

    def __init__(self):
        pass


def check_response(possible_responses: list):
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

        if response == 'r':
            clear_console()
            start()

        if response == 'h':
            help()
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


def help():
    """Help menu."""

    print(colored('At any time you can use the following commands:\n    h --help menu\n    r --restart from the beginning\n    q --quit game', opt.event_color))


def start():
    """Start menu."""

    start_actions = [f'Play as {opt.name}', 'Options', 'Help', 'Quit']
    p_r = []
    print(colored('Welcome to the Survival of the Weirdest!', opt.event_color))

    print_actions(start_actions, p_r)
    r = check_response(p_r)

    if r == 1:
        clear_console()
        event_1()

    elif r == 2:
        clear_console()
        options()

    elif r == 3:
        clear_console()
        help()
        start()

    elif r == 4:
        print(colored('Quitting...', opt.event_color))
        sys.exit()


def restart():
    """Restart menu."""

    print(colored('Would you like to play again?'), opt.event_color)

    p_r = []

    e_actions = ['Yes',
                 'No']

    print_actions(e_actions, p_r)
    responses.restart = check_response(p_r)

    if responses.restart == 1:
        clear_console()
        start()

    elif responses.restart == 2:
        clear_console()
        print(colored('Thanks for playing!'), opt.event_color)
        sys.exit()


def options():
    """Options menu."""

    opt_actions = [f'Name: {opt.name}', f'Event Color: {opt.event_color}',
                   f'Actions Color: {opt.actions_color}', 'Back']
    p_r = []

    print_actions(opt_actions, p_r)
    r = check_response(p_r)

    if r == 1:
        opt.name = input(colored('New name > ', opt.actions_color))
        clear_console()
        options()

    elif r == 2:
        print(
            colored('Colors: ', opt.event_color) + colored(f'{", ".join(opt.all_colors)}', opt.actions_color))

        print(
            colored('New event color:', opt.event_color))

        opt.event_color = check_response(opt.all_colors)

        clear_console()
        options()

    elif r == 3:
        print(
            colored('Colors: ', opt.event_color) + colored(f'{", ".join(opt.all_colors)}', opt.actions_color))

        print(
            colored('New actions color:', opt.event_color))

        opt.actions_color = check_response(opt.all_colors)

        clear_console()
        options()

    elif r == 4:
        clear_console()
        start()


def event_1():
    print(
        colored('Welcome to "Survival of the Weirdest"! You wake up on a deserted beach with nothing but the clothes on your back and a few scraps of debris washed up on shore. You can see that the island is covered in a thick jungle, and you can hear strange noises coming from within.', opt.event_color))

    p_r = []

    e_actions = ['Explore the jungle', 'Build a shelter on the beach',
                 'Collect food and water from the surrounding area']

    print_actions(e_actions, p_r)
    responses.e_1 = check_response(p_r)

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

    e_actions = ['Investigate the giggling sounds.',
                 'Avoid the giggling and keep moving forward.',
                 'Go back to the beach.', ]

    print_actions(e_actions, p_r)
    responses.e_2 = check_response(p_r)

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

    print(colored('As you approach the treehouse, you suddenly feel yourself falling through a hidden trapdoor in the ground. You land with a thud on a hard surface, and realize that youre in some kind of underground chamber. The door above you slams shut, leaving you in complete darkness.You hear a voice coming from somewhere in the chamber. "Welcome to your new home," the voice says.', opt.event_color))
    print(colored('"Youre never leaving." Game over.', opt.event_color))


def event_5():
    clear_console()

    p_r = []

    e_actions = ['Investigate the rustling in the bushes',
                 'Continue building the shelter',
                 'Look for more resources on the beach.', ]

    print(colored('You begin gathering driftwood, palm fronds, and any other materials you can find to build your shelter. As you work, you hear rustling in the nearby bushes.', opt.event_color))

    print_actions(e_actions, p_r)
    responses.e_5 = check_response(p_r)

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

    e_actions = ['Investigate the rustling in the bushes',
                 'Look for more resources on the beach.', ]

    print_actions(e_actions, p_r)
    responses.e_7 = check_response(p_r)

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

    e_actions = ['Ignore the coconut and keep searching for resources',
                 'Talk to the coconut and ask for help',
                 'Take a bite out of the coconut, thinking it will solve your hunger problem.']

    print_actions(e_actions, p_r)
    responses.e_7 = check_response(p_r)

    if responses.e_7 == 1:
        clear_console()
        event_9()

    elif responses.e_7 == 2:
        clear_console()
        event_10()

    elif responses.e_7 == 3:
        clear_console()
        event_11()


def event_9():
    clear_console()

    print(colored('You decide to ignore the talking coconut and continue your search for resources. You are getting hungry and thirsty, but you are determined to find what you need to survive. But its too late, you start feeling dizzy and weak. Your body gives up and you collapse on the sand, unable to move any further. It seems like you have succumbed to dehydration and starvation.', opt.event_color))
    print(colored('Game over.', opt.event_color))


def event_10():
    clear_console()

    print(colored('You decide to talk to the coconut and ask for help. The coconut introduces itself as Sir Reginald and asks how he can be of assistance. You explain your situation and Sir Reginald suggests that you eat him. \n You are taken aback by Sir Reginalds suggestion and tell him that you cannot eat a talking coconut. Sir Reginald chuckles and says, "please, you have to" \nYou are hesitant, but as you look around and realize that you have no other source of food, you reluctantly take a bite out of Sir Reginald. To your surprise, he tastes delicious and you feel a surge of energy as you eat. \nSir Reginald chuckles again and says, "I told you, old chap. I may be unusual, but I am quite tasty."', opt.event_color))

    event_11_2()


def event_11():
    clear_console()

    print(colored('You take a bite out of the coconut, but as you do, the coconut opens its eyes and screams in agony! Now you have energy. You continue searching for resources. As you explore the area, you come across an Excalibur.', opt.event_color))

    p_r = []

    e_actions = [' Embrace your new role as Excaliburs wielder and set out to explore the island and find a way to escape.',
                 'Throw the sword away, thinking it is just a hallucination.']

    print_actions(e_actions, p_r)
    responses.e_11 = check_response(p_r)

    if responses.e_11 == 1:
        clear_console()
        event_12()

    if responses.e_11 == 2:
        clear_console()
        event_5()


def event_11_2():
    clear_console()

    print(colored('Now you have energy. You continue searching for resources. As you explore the area, you come across an Excalibur.', opt.event_color))

    p_r = []

    e_actions = ['Embace your new role as Excaliburs wielder and set out to explore the island and find a way to escape.',
                 'Throw the sword away, thinking it is just a hallucination.']

    print_actions(e_actions, p_r)
    responses.e_11 = check_response(p_r)

    if responses.e_11 == 1:
        clear_console()
        event_12()

    if responses.e_11 == 2:
        clear_console()
        event_5()


def event_12():
    clear_console()

    print(colored('You pick up the Excalibur and feel a surge of power course through you. With newfound confidence, you set out to explore the island and find a way to escape.\nAs you trek through the jungle, you come across a band of monkeys dressed in pirate attire. They are led by a particularly large monkey wearing a captains hat.\nThe monkey captain says, "Arrr, ye be tresspassin on our island! Surrender yer booty or face the consequences!"', opt.event_color))

    p_r = []

    e_actions = ['Stand your ground and brandish Excalibur, daring the monkeys to attack.',
                 'Offer the monkeys some of the resources you collected in exchange for safe passage through their territory.',
                 'Try to negotiate with the monkey captain and persuade him to let you join their pirate crew.']

    print_actions(e_actions, p_r)
    responses.e_12 = check_response(p_r)

    if responses.e_12 == 1 and responses.e_5 == 2:
        clear_console()
        event_13()

    elif responses.e_12 == 1:
        clear_console()
        event_14()

    elif responses.e_12 == 2:
        clear_console()
        event_15()

    elif responses.e_12 == 3:
        clear_console()
        event_16()


def event_13():
    clear_console()

    print(colored('You stand your ground and brandish Excalibur, daring the monkeys to attack. The monkey captain laughs and orders his crew to charge.\nThe monkeys swarm towards you, but with swift and precise strikes of Excalibur, you manage to take down several of them. The rest of the monkeys see your ferocity and intelligence and decide to retreat.\nBut when its all over, a giant bird descends from the sky and snatches Excalibur from your hand with its talons, flying off into the jungle.\nYou start to run, but where do you hide?', opt.event_color))

    p_r = []

    e_actions = ['Under a rock.',
                 'Under some grass. ',
                 'In your shelter.']

    print_actions(e_actions, p_r)
    responses.e_13 = check_response(p_r)

    if responses.e_13 == 1:
        clear_console()
        event_17()

    elif responses.e_13 == 2:
        clear_console()
        event_18()

    elif responses.e_13 == 3:
        clear_console()
        event_19()


def event_14():
    clear_console()

    print(colored('You stand your ground and brandish Excalibur, daring the monkeys to attack. The monkey captain laughs and orders his crew to charge.\nThe monkeys swarm towards you, but with swift and precise strikes of Excalibur, you manage to take down several of them. The rest of the monkeys see your ferocity and intelligence and decide to retreat.\nBut when its all over, a giant bird descends from the sky and snatches Excalibur from your hand with its talons, flying off into the jungle.\nYou start to run, but where do you hide?', opt.event_color))

    p_r = []

    e_actions = ['Under a rock.',
                 'Under some grass. ']

    print_actions(e_actions, p_r)
    responses.e_13 = check_response(p_r)

    if responses.e_13 == 1:
        clear_console()
        event_17()

    elif responses.e_13 == 2:
        clear_console()
        event_18()


def event_15():
    clear_console()

    print(colored('As you try to negotiate with the monkey captain and offer them some of the resources you collected, the monkeys suddenly become aggressive and attack you, taking all of your belongings.\nUnable to defend yourself without any weapons or resources, the monkeys overpower you, and you quickly succumb to your injuries.\nGame Over.', opt.event_color))


def event_16():
    clear_console()

    print(colored('You decide to negotiate with the monkey captain and ask to join their pirate crew. The captain looks you over for a moment, then nods his head and says, "Aye, we be needin some fresh blood on the crew. Ye be welcome to join us, matey!"\nYou spend the next few years living out your life as a pirate, going on thrilling adventures, and looting treasure. Eventually, you become known as one of the most fearsome pirates on the high seas.\nHowever, the desire to escape the island and return to civilization still burns within you. One day, you come across a map that leads to a hidden treasure trove. You convince the monkey captain and the rest of the crew to join you on the expedition.\nAfter braving treacherous storms and fending off rival pirate crews, you finally discover the treasure trove. The treasure is enough to buy you all tickets back to civilization.\nYou and the monkey pirates bid farewell to the island and set sail, ready for new adventures. \nThe end.'), opt.event_color)


def event_17():
    clear_console()

    print(colored('You quickly hide under a nearby rock, trying to catch your breath and assess the situation. However, the giant bird manages to locate you and swoops down, snatching you up in its talons and carrying you off to its nest high up in the jungle canopy.\nAs you sit in the birds nest, surrounded by its offspring, you realize that escape may be impossible. You have been trapped on the island with seemingly no hope of rescue. \nGame over.'), opt.event_color)


def event_18():
    clear_console()

    print(colored('You quickly dive under some nearby grass, hoping to stay hidden from the giant bird. However, the bird spots you and swoops down, grabbing you with its talons before flying off into the jungle.\nYour adventure on the island comes to a tragic end. \nGame over!', opt.event_color))


def event_19():
    clear_console()

    print(colored('You quickly run to your shelter, but as you do, you notice that the giant bird has dropped Excalibur in the midst of the jungle. You hide inside your shelter, heart pounding with fear and uncertainty.\nAfter a few minutes, you hear a strange scratching noise outside. You cautiously peek outside and are surprised to see the giant bird, staring at you with curious eyes.\mSuddenly, an idea comes to mind. You remember hearing stories of people taming animals for travel or companionship. Perhaps you can do the same with this bird!\nYou slowly and carefully approach the bird, holding out your hand in a gesture of peace. To your amazement, the bird approaches you, and after a few minutes of tentative sniffing, allows you to pet him.\nWith a sudden burst of daring, you climb onto the birds back and take flight. Your new feathered friend carries you over the dense jungle, and after a few hours of flight, you are finally rescued by a passing ship.\nCongratulations on surviving and escaping the deserted island!', opt.event_color))


opt = store_options('Player', 'white', 'green')
responses = store_responses()

if __name__ == '__main__':
    clear_console()
    start()
    restart()
