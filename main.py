import random
from colorama import Fore, Style

class BitcoinGenerator:
    def __init__(self):
        self.balance = 1000  # Starting balance for the generator

    def generate_bitcoin(self, amount):
        if amount > 0:
            self.balance -= amount
            return True
        return False

class BitcoinSender:
    def send_bitcoin(self, address, amount):
        # Simulating sending bitcoin
        if address and amount > 0:
            return True
        return False

def main():
    generator = BitcoinGenerator()
    sender = BitcoinSender()

    try:
        print("Bitcoin Generator and Sender")
        address = input("Enter the bitcoin address: ")
        amount = float(input("Enter the amount of bitcoin to generate and send: "))

        if generator.generate_bitcoin(amount):
            if sender.send_bitcoin(address, amount):
                print(Fore.GREEN + "Bitcoin sent successfully!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Failed to send bitcoin. Please check the address." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid amount. Please enter a positive value." + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
