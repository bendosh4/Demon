# Demon v1.1
## Documentation
**Make sure to check the documentation for more info [documentation](https://bendosh4.github.io/Demon-Website/)**
## Description

**Demon** is a Python project that consists of three major components: encryption with a random key, port scanning, and file management. This project demonstrates various techniques in Python, including cryptography, network scanning, and file handling.

## Features

1. **Encryption with Random Key:**
   - Implements encryption algorithms to secure data using a randomly generated key.
   - Provides functionality to encrypt and decrypt data securely.

2. **Port Scanning:**
   - Scans specified IP addresses or ranges to identify open ports.
   - Helps in assessing network security and discovering services running on a network.

3. **File Management:**
   - Provides functionality for reading, writing, and managing files.
   - Includes operations such as file creation, deletion, and updating file content.
   - Could also integrate with encryption features to securely handle file data.

## Technologies Used

- **Python:** For implementing encryption algorithms, port scanning, and file management functionalities.
- **Libraries Used:**
  - `colors`: A custom file for ASCII colors.
  - `random`: For generating random keys.
  - `port_scanner`: A custom file for port scanning functionality.
  - `datetime`: For handling date and time operations.
  - `logo`: A custom file for displaying logos.
  - `extra`: A custom file for additional functionalities.
  - `threading`: For concurrent execution.
  - `subprocess`: For executing shell commands.
  - `keyboard`: For keyboard event handling.

## Getting Started

To get started with the project:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/bendosh/Demon.git
    ```

2. **Navigate to the Project Directory:**
    ```sh
    cd Demon
    ```

3. **Install Dependencies:**
    - Make sure you have Python installed.
    - Install required Python packages using `pip`:
      ```sh
      pip install -r requirements.txt
      ```

4. **Run the Application:**
    - To run the application, execute the `Demon.py` script:
      ```sh
      python Demon.py
      ```

## Installation on Different Virtual Machines

### Ubuntu/Debian-based VMs

```sh
# Update Package List
sudo apt update

# Install Python and Pip
sudo apt install -y python3 python3-pip

# Clone the Repository
git clone https://github.com/bendosh/Demon.git
cd Demon

# Install Dependencies
pip3 install -r requirements.txt

# Run the Application
python3 Demon.py
```

### CentOS/RHEL-based VMs

```sh
# Update Package List
sudo yum update -y

# Install Python and Pip
sudo yum install -y python3 python3-pip

# Clone the Repository
git clone https://github.com/bendosh/Demon.git
cd Demon

# Install Dependencies
pip3 install -r requirements.txt

# Run the Application
python3 Demon.py
```

### Windows VMs

```sh
# Install Python (Manual Steps)
# - Download and install Python from the official Python website: https://www.python.org/downloads/
# - Ensure to check the box to add Python to your PATH during installation

# Clone the Repository
git clone https://github.com/bendosh/Demon.git
cd Demon

# Install Dependencies
pip install -r requirements.txt

# Run the Application
python Demon.py
```

## Commands

Once you have the application running, you can use the following commands:

- `port scanning`: Initiates a port scan on the specified IP addresses or ranges.
- `clear`: Clears the console screen.
- `help`: Displays a help message with available commands and their usage.
- `last`: Shows the last command executed.
- `time`: Displays the current system time.
- `encryption`: Encrypts data using a randomly generated key.
- `decryption`: Decrypts data using the previously generated key.
- `exit`: Exits the application.
- `read`: Reads and displays the content of a specified file.

## Upcoming
Hash decryption - decrypt hash for more then 10 types! 
binary to hexdecimal - caculator for binary to hexdecimal
upgrading file encryption - file encryption system will take a step up!

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## About Me

My name is Yarin, and I am a 15-year-old developer from Israel. I am passionate about programming and have experience with C, C++, and Python. I am continuously learning and exploring new technologies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
