import colors
import random
import port_scanner
import datetime

def pront_cmd():
    commends = ['port scanning', 'network discovery', 'vulnerability scanning', 'pen test', 'exploit development']
    for c in commends:
        print(f"{colors.COLORS['cyan']}{c}{colors.RESET}")
        


def print_logo():
    toPrint = """


    .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |  ________    | || |  _________   | || | ____    ____ | || |     ____     | || | ____  _____  | |
    | | |_   ___ `.  | || | |_   ___  |  | || ||_   \  /   _|| || |   .'    `.   | || ||_   \|_   _| | |
    | |   | |   `. \ | || |   | |_  \_|  | || |  |   \/   |  | || |  /  .--.  \  | || |  |   \ | |   | |
    | |   | |    | | | || |   |  _|  _   | || |  | |\  /| |  | || |  | |    | |  | || |  | |\ \| |   | |
    | |  _| |___.' / | || |  _| |___/ |  | || | _| |_\/_| |_ | || |  \  `--'  /  | || | _| |_\   |_  | |
    | | |________.'  | || | |_________|  | || ||_____||_____|| || |   `.____.'   | || ||_____|\____| | |
    | |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


    """

    for line in toPrint.split("\n"):
        random_color = random.choice(list(colors.COLORS.values()))
        print(f"{random_color}{line}{colors.RESET}")


print_logo()
print(f"{colors.COLORS['green']}Welcome to the Demon!{colors.RESET}")
print(f"{colors.COLORS['blue']}Type 'exit' to quit the program\nhelp for commends{colors.RESET}")
msg = ''

while msg != "exit":
    msg = input(f"{colors.COLORS['yellow']}> {colors.RESET}")
    
    if msg == "help":
        pront_cmd()
    elif msg == "port scanning":
        port_scanner.scan()
    elif msg == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{colors.COLORS['magenta']}The current time is {current_time}{colors.RESET}")
    elif msg == "color":
        random_color = random.choice(list(colors.COLORS.values()))
        print(f"{random_color}Random color selected{colors.RESET}")
    elif msg == "exit":
        print(f"{colors.COLORS['green']}Goodbye, Demon!{colors.RESET}")
    else:
        print(f"{colors.COLORS['red']}Invalid command. Type 'help' for available commands.{colors.RESET}")