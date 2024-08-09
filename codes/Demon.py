import colors
import random
import port_scanner
import datetime
import logo
import extra
import threading  
import subprocess
import fileEncrypter

def pront_cmd():
    commends = ['port scanning', 'clear', 'help', 'last', 'time', 'encryption', 'decryption', 'exit', 'read', 'hash decrypter']
    for c in commends:
        print(f"{colors.COLORS['cyan']}{c}{colors.RESET}")
        
        
logo.print_logo()
extra.unzip_start_file()
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
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{colors.COLORS['magenta']}The current time is {current_time}{colors.RESET}")
    elif msg == "encryption":
        fileEncrypter.encrypt()
    elif msg == "decryption":
        fileEncrypter.decrypt()
    elif msg == 'read':
        fileEncrypter.read()
    elif msg == "hash decrypter":
        fileEncrypter.HashDecypter()
    elif msg == "exit":
        print(f"{colors.COLORS['green']}Goodbye, Demon!{colors.RESET}")
    else:
        extra.wrong_commend(msg)