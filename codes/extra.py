import keyboard
import colors

last_typed_commend = []

def arrow_keys_pressed(last_pressed_cmd: list) -> bool:
    while True:
        if keyboard.is_pressed('-'):
            print(f"{colors.COLORS['yellow']}Previous command: {last_pressed_cmd[-1]}{colors.RESET}")
                        


