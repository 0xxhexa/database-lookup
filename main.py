import os
import colorama
from colorama import Fore

def search_files(folder, search_input):
    for root, _, files in os.walk(folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_input in line:
                        print(f"\n{Fore.LIGHTGREEN_EX}{file_name}\n{Fore.LIGHTCYAN_EX}{line.strip()}")
                        
def main():
    colorama.init()
    print(f"{Fore.RED}\n\n██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ ")
    print(f"{Fore.RED}██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗")
    print(f"{Fore.RED}██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝")
    print(f"{Fore.RED}██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ ")
    print(f"{Fore.RED}███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     ")
    print(f"{Fore.RED}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ")
    folder = ("search")
    search_input = input(f"\n{Fore.GREEN}Lookup: {Fore.LIGHTGREEN_EX}")
    search_files(folder, search_input)
    main()

os.system('cls')
main()
