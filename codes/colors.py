
# Define ANSI escape codes
RESET = "\033[0m"

# Text colors
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

# Background colors
BG_COLORS = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}

# Styles
STYLES = {
    "reset": "\033[0m",
    "bright": "\033[1m",
    "dim": "\033[2m",
    "underlined": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "hidden": "\033[8m",
}

def print_colored_text():
    # Display all text colors
    print("Text Colors:")
    for color_name, color_code in COLORS.items():
        print(f"{color_code}{color_name.capitalize()}{RESET}")

    # Display all background colors
    print("\nBackground Colors:")
    for color_name, bg_color_code in BG_COLORS.items():
        print(f"{bg_color_code} {color_name.capitalize()} {RESET}")

    # Display all styles
    print("\nStyles:")
    for style_name, style_code in STYLES.items():
        print(f"{style_code}{style_name.capitalize()}{RESET}")

    # Combine text colors, background colors, and styles
    print("\nCombined Text Colors, Background Colors, and Styles:")
    for text_color_name, text_color_code in COLORS.items():
        for bg_color_name, bg_color_code in BG_COLORS.items():
            for style_name, style_code in STYLES.items():
                combined_text = f"{style_code}{text_color_code}{bg_color_code} {style_name.capitalize()} {text_color_name.capitalize()} on {bg_color_name.capitalize()} {RESET}"
                print(combined_text)

if __name__ == "__main__":
    print_colored_text()
