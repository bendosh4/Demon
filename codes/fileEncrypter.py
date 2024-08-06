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
import colors
import string
import random
import os
import hashlib

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

def check_password(password, hashType, hashValue):
    hashedPassword = hashlib.new(hashType, password.encode()).hexdigest()
    return hashedPassword == hashValue

def HashDecypter():
    hashTypes = ['sha3_512', 'sha1', 'sha224', 'sha3_384', 'sha512', 'sha384', 'blake2s', 'md5', 'sha3_224', 'sha256', 'blake2b', 'sha3_256', 'shake_128']

    print(f"{colors.BG_COLORS['yellow']}Available hash functions:{colors.RESET}")
    for hashType in hashTypes:
        print(f"{colors.COLORS['blue']}* {hashType}{colors.RESET}")
    
    print(f"{colors.COLORS['red']}If you don't know the hash type, enter 'None'{colors.RESET}")
    
    hashType = input(f"{colors.BG_COLORS['yellow']}Enter hash function to decrypt:{colors.RESET} ")
    if hashType not in hashTypes and hashType != 'None':
        print(f"{colors.BG_COLORS['red']}Invalid hash function. Please try again.{colors.RESET}")
        return
    
    passwordFileToBruteForce = 'wordlist_ziped/rockyou.txt'
    
    if not os.path.isfile(passwordFileToBruteForce):
        print(f"{colors.BG_COLORS['red']}Password file not found. Please make sure the file exists at {passwordFileToBruteForce}{colors.RESET}")
        return
    
    hashValue = input(f"{colors.BG_COLORS['yellow']}Enter hashed value to decrypt:{colors.RESET} ")
    
    def sit_TIGHT():
        print(f"{colors.BG_COLORS['yellow']}We are checking out for more than 100 million potential passwords...\nThis might take some time!...{colors.RESET}")
    
    def normal_hash_decrypt(passwordFileToBruteForce, hashType, hashValue):
        found = False
        batch_size = 1000
        with open(passwordFileToBruteForce, 'r', encoding='utf-8', errors='ignore') as file:
            batch = []
            for password in file:
                batch.append(password.strip())  # Remove any extra whitespace or newlines
                if len(batch) >= batch_size:
                    # Process the current batch
                    for pwd in batch:
                        if check_password(pwd, hashType, hashValue):
                            print(f"{colors.BG_COLORS['green']}Decrypted password found: {colors.COLORS['cyan']}{pwd}{colors.RESET}")
                            found = True
                            return True
                    batch = []

            # Process any remaining passwords in the last batch
            if not found:
                for pwd in batch:
                    if check_password(pwd, hashType, hashValue):
                        print(f"{colors.BG_COLORS['green']}Decrypted password found: {colors.COLORS['cyan']}{pwd}{colors.RESET}")
                        found = True
                        return True
        return False

    sit_TIGHT()
    
    batch_size = 1000
    if hashType == 'None':
        for hashType in hashTypes:
            print(f"{colors.COLORS['blue']}Started scanning Hash type: {hashType}{colors.RESET}")
            found = normal_hash_decrypt(passwordFileToBruteForce, hashType, hashValue)
            if found:
                return
        print(f"{colors.BG_COLORS['red']}No decrypted password found in the password file.{colors.RESET}")
    else:
        found = normal_hash_decrypt(passwordFileToBruteForce, hashType, hashValue)
        if not found:
            print(f"{colors.BG_COLORS['red']}Password not found in the password file.{colors.RESET}")
