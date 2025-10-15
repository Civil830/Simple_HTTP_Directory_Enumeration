import subprocess
import re


def main():
    # Start the program
    print("Starting the program...")

    # Input network IP address
    target_ip = input("Enter the target IP address to scan (e.g., 192.168.1.1): ")

    # Run nmap and export results into a text file
    print("Running nmap scan...")
    subprocess.run(["nmap", "-oN", "nmap_results.txt", target_ip])

    # Read the text file
    with open("nmap_results.txt", "r") as file:
        nmap_output = file.read()

    # Find IP address with port 80 open
    ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", nmap_output)

    # If port 80 is open, then gobuster will be used to enumerate the target IP.
    if ip_match and "80/tcp" in nmap_output and "open" in nmap_output:
        ip_address = ip_match.group()
        user_input = input(f"Port 80 is open on {ip_address}. Do you want to include a starting web directory (e.g., /foo)? YES/NO: ")
        if user_input.lower() == "yes":
            directory_input = input("Enter the starting web directory (Will require a '/' to be entered): ")
            ip_address = ip_address + directory_input

        print("Running gobuster...")
        subprocess.run(["gobuster", "dir", "-u", f"http://{ip_address}", "-w",
                        "/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt"])

    else:
        print("Port 80 is not open on any IP address. Doing nothing.")

    # Terminate the program
    print("Terminating the program...")


if __name__ == "__main__":
    main()
