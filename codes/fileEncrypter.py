import colors
import string
import random
import os
import subprocess

def read():
    filePath = input(f"{colors.BG_COLORS['yellow']}Enter file path to read:{colors.RESET} ")
    if not os.path.isfile(filePath):
        print(f"{colors.BG_COLORS['red']}File not found. Please check the file path and try again.{colors.RESET}")
        return
    with open(filePath, 'r') as file:
        data = file.read()
    print(f"{colors.BG_COLORS['green']}File read successfully!\nData: {colors.COLORS['cyan']}{data}{colors.RESET}")

def decrypt():
    key = input(f"{colors.BG_COLORS['yellow']}Enter encryption key:{colors.RESET} ")
    filePath = input(f"{colors.BG_COLORS['yellow']}Enter file path to decrypt:{colors.RESET} ")
    decryptedFilePath = input(f"{colors.BG_COLORS['yellow']}Enter file path to save decrypted data: {colors.RESET}") 
    
    if not os.path.isfile(filePath):
        print(f"{colors.BG_COLORS['red']}File not found. Please check the file path and try again.{colors.RESET}")
        return
    
    decryptedData = ""
    with open(filePath, 'r') as file:
        data = file.read()
    for num in key:
        data = ceaserCipher(int(num), data, 'decrypt')
        decryptedData = data
    with open(decryptedFilePath, 'w') as file:
        file.write(decryptedData)

        print(f"{colors.BG_COLORS['green']}Decryption successful!\nYou can check out the new file at {decryptedFilePath}{colors.RESET}")
    

def createKey():
    keyLen = random.randint(20, 30)
    key = ''.join(random.choices(string.digits, k=keyLen))
    print(f"{colors.COLORS['green']}Encryption key generated successfully!\nYour encryption key is: {colors.COLORS['red']}{key}{colors.RESET}")
    return key
    
def encrypt():
    key = createKey()
    data = ""
    fileToEncrypt = input(f"{colors.BG_COLORS['yellow']}{colors.STYLES['bright']}Enter file path to encrypt:{colors.RESET} ")
    with open(fileToEncrypt, 'r') as file:
        data = file.read()
    os.remove(fileToEncrypt)
    with open(fileToEncrypt, 'w') as file:
        for num in key:
            data = ceaserCipher(int(num), data, 'encrypt')
        file.write(data)
        
        print(f"{colors.BG_COLORS['green']}Encryption successful!\nYou can check out the new file at {fileToEncrypt}{colors.RESET}")
    
    
def ceaserCipher(key, data, direction):
    if direction == 'encrypt':
        encryptedData = ""
        for char in data:
            if char.isalpha():
                asciiVal = ord(char)
                asciiVal += key
                if char.isupper():
                    encryptedData += chr((asciiVal - 65) % 26 + 65)
                else:
                    encryptedData += chr((asciiVal - 97) % 26 + 97)
            else:
                encryptedData += char
        return encryptedData
    elif direction == 'decrypt':
        decryptedData = ""
        for char in data:
            if char.isalpha():
                asciiVal = ord(char)
                asciiVal -= key
                if char.isupper():
                    decryptedData += chr((asciiVal - 65) % 26 + 65)
                else:
                    decryptedData += chr((asciiVal - 97) % 26 + 97)
            else:
                decryptedData += char
        return decryptedData
