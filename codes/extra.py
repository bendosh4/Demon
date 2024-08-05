import keyboard
import colors

last_typed_commend = []

def wrong_commend(commend):
    #print(f"{commend} is not a valid command. Type 'help' for available commands.")
    if 'port' in commend or 'scanning' in commend:
        print(f"{colors.COLORS['red']}{commend} Did you mean 'port scanning'?{colors.RESET}")
    else:
        print(f"{colors.COLORS['red']}Invalid command. Type 'help' for available commands.{colors.RESET}")