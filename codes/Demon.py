import colors
import random
import port_scanner
import datetime
import logo
import extra
import threading  
import subprocess

def pront_cmd():
    commends = ['port scanning', 'network discovery', 'vulnerability scanning', 'pen test', 'exploit development']
    for c in commends:
        print(f"{colors.COLORS['cyan']}{c}{colors.RESET}")
        
        
logo.print_logo()
print(f"{colors.COLORS['green']}Welcome to the Demon!{colors.RESET}")
print(f"{colors.COLORS['blue']}Type 'exit' to quit the program\nhelp for commends{colors.RESET}")
msg = ''

while msg != "exit":
    msg = input(f"{colors.COLORS['yellow']}> {colors.RESET}")
    extra.last_typed_commend.append(msg)
    if msg == "last":
        print(f"{colors.COLORS['yellow']}Last 5 typed commands:{colors.RESET}")
        for i, c in enumerate(extra.last_typed_commend[:-1], start=1):
            print(f"{i}. {c}")
        
    elif msg == "clear":
        subprocess.call('clear', shell=True)
        logo.print_logo()
        print(f"{colors.COLORS['green']}Welcome to the Demon!{colors.RESET}")
        print(f"{colors.COLORS['blue']}Type 'exit' to quit the program\nhelp for commends{colors.RESET}")
    elif msg == "help":
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