import socket
import subprocess
import sys
from datetime import datetime
import threading
import colors
import logo



def scan():
    # Clear screen
    subprocess.call('clear', shell=True)

    logo.print_logo()
    remoteServer = input("Enter a remote server: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    print(f"{colors.COLORS['cyan']}IP address of {remoteServer}: {remoteServerIP}{colors.RESET}")

    print(f"{colors.COLORS['yellow']}----------------------------------------------------{colors.RESET}")
    print(f"{colors.COLORS['green']}Scanning ports on {remoteServer} ({remoteServerIP}){colors.RESET}")
    print(f"{colors.COLORS['yellow']}----------------------------------------------------{colors.RESET}")

    startTime = datetime.now()

    # Thread function to scan a port
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print(f"{colors.COLORS['green']}Port {port} is open{colors.RESET}")
            sock.close()
        except socket.error:
            print(f"{colors.COLORS['red']}Couldn't connect to port {port}{colors.RESET}")

    # Create and start threads for port scanning
    threads = []
    for port in range(1, 5000):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    endTime = datetime.now()
    totalTime = endTime - startTime

    print(f"{colors.COLORS['yellow']}----------------------------------------------------{colors.RESET}")
    print(f"{colors.COLORS['green']}Port scanning completed in {totalTime.seconds} seconds{colors.RESET}")
    print(f"{colors.COLORS['yellow']}----------------------------------------------------{colors.RESET}")