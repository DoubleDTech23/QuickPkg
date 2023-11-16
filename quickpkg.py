import subprocess
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def search_package(package_name):
    try:
        subprocess.run(['apt', 'search', package_name])  # For Debian-based systems
        # If you want to add support for Red Hat-based systems, you can use 'yum search' here
    except FileNotFoundError:
        print("Package management tool not found. This tool currently supports Debian-based systems.")

def install_package(package_name):
    try:
        subprocess.run(['sudo', 'apt', 'install', package_name])  # For Debian-based systems
        # If you want to add support for Red Hat-based systems, you can use 'sudo yum install' here
    except FileNotFoundError:
        print("Package management tool not found. This tool currently supports Debian-based systems.")

# Colored prompts
def input_prompt(prompt):
    return input(Fore.CYAN + Style.BRIGHT + prompt + Style.RESET_ALL)

# Main program
if __name__ == "__main__":
    print(Fore.GREEN + Style.BRIGHT + "Welcome to QuickPkg!" + Style.RESET_ALL)

    action = input_prompt("Enter 's' to search for a package, 'i' to install a package: ")

    if action == 's':
        package_name = input_prompt("Enter the package name to search: ")
        search_package(package_name)
    elif action == 'i':
        package_name = input_prompt("Enter the package name to install: ")
        install_package(package_name)
    else:
        print(Fore.RED + "Invalid action. Please enter 's' or 'i'." + Style.RESET_ALL)
