# Simple_HTTP_Directory_Enumeration
A simple Python script that automates the process of scanning the open ports of a target IP address with nmap and if port 80 (HTTP) is detected as open, it will use gobuster to enumerate the possible web directories.

# Prerequisites
This script will require the following:
- Python 3.x
- nmap
- gobuster
- A wordlist for possible web-directories (can be changed within the code, a wordlist from Kali's dirbuster wordlist folder has been used as the default wordlist).

# Running the script:
You will have to enter the following prompts.
- Enter the target IP address (e.g., 192.168.1.1).
- If port 80 is open, you can decide if you want to include a starting directory.
- If you choose yes, then you will have to enter the directory path (it must start with /, e.g., /admin).
