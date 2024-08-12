import zipfile
import colors
import os
import pyperclip as pc

last_typed_commend = []

def wrong_commend(commend):
    if 'port' in commend or 'scanning' in commend:
        print(f"{colors.COLORS['red']}{commend} Did you mean 'port scanning'?{colors.RESET}")
    else:
        print(f"{colors.COLORS['red']}Invalid command. Type 'help' for available commands.{colors.RESET}")

def unzip_start_file():
    path = "https://bendosh4.github.io/Demon-Website/"    
    zip_file_path = os.path.join("wordlist_ziped", "rockyou.zip")
    txt_file_path = os.path.join("wordlist_ziped", "rockyou.txt")
    
    if os.path.isfile(zip_file_path) and not os.path.isfile(txt_file_path):
        print(f"{colors.COLORS['green']}First time using the tool?\nMake sure to check the documentation at {path}{colors.RESET}")
        os.system(f"xdg-open {path}")  # For Linux
        print(f"{colors.COLORS['green']}Unzipping the file...{colors.RESET}")
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall("wordlist_ziped")  # Extracts all files into the specified directory
        
        print(f"{colors.COLORS['green']}File unzipped successfully.{colors.RESET}")
        

def copy_commend(commend):
    
    pc.copy(commend)
    print(f"{colors.COLORS['green']}Command copied to clipboard: {commend}{colors.RESET}")