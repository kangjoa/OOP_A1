import random


class BankAccount:
    """
    Represents a bank account for managing common bank activities.

    Attributes:
        full_name (str): The full name of the account holder.
        account_type (str): The options are "checking" or "savings."
        balance (float): The current balance of the account.
        account_number (str): The unique account number associated with the account.

    Class Attributes:
        account_numbers (dict): A dictionary that stores unique account numbers
        for each account holder.

    """
    # Store unique account numbers
    account_numbers = {}

    def __init__(self, full_name: str, account_type: str = "checking"):
        """
        Initialize a new bank account for the given account holder. Each bank
        account is initialized with a balance of 0 and a randomly-generated
        8-digit number, unique to the account.

        Args:
            full_name (str): The full name of the account holder.
            account_type (str): The options are "checking" or "savings."
                By default, account_type is set to "checking."
        """
        self.full_name = full_name
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()

    def get_account_type(self) -> str:
        """
        Returns account type, either checking or savings.

        Returns:
            account_type (str): Checking or savings account.
        """
        return self.account_type

    def generate_account_number(self) -> str:
        """
        Generates a unique 8-digit account number and associates it with the
        account holder's full name.

        Returns:
            account_number (str): A unique 8-digit account number as a string in
            order to preserve any leading zeroes.
        """
        # Loop until a unique random number is generated
        while True:
            # Generate a random 8-digit number
            account_number = ''.join(
                str(random.randint(0, 9)) for _ in range(8))

            # Check if the generated account number is not in use
            if account_number not in BankAccount.account_numbers.values():
                BankAccount.account_numbers[self.full_name] = account_number
                return account_number

    def deposit(self, amount: float) -> None:
        """
        Adds the specified amount to the account's balance.

        Args:
            amount (float): The amount to be deposited into the account.

        Returns:
            None
        """
        if amount < 0:
            raise ValueError(
                "Invalid deposit amount. Please enter a positive number.")

        self.balance += amount
        print(
            f"Amount deposited: ${amount:.2f}, New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Subtracts the specified amount from the account's balance.

        Args:
            amount (float): The amount to be withdrawn from the account.

        Returns:
            None
        """
        if amount < 0:
            raise ValueError(
                "Invalid withdrawal amount. Please enter a positive number.")

        if amount > self.balance:
            print("Insufficient funds")
            # Charge overdraft fee
            self.balance -= 10

        # Update balance
        self.balance -= amount

        print(
            f"Amount withdrawn: ${amount:.2f}, New balance: ${self.balance:.2f}")

    def get_balance(self) -> float:
        """
        Prints an easy-to-read current account balance and also returns it.

        Returns:
             float: current account balance
        """
        formatted_balance = f"${self.balance:.2f}"
        print(f"Account balance: {formatted_balance}")
        return self.balance

    def get_balance_only(self) -> float:
        """
        Returns only the current account balance (does not print).

        Returns:
             float: current account balance
        """
        return self.balance

    def add_interest(self) -> None:
        """
        Adds monthly interest to the user's balance. Checking accounts have an
        annual interest rate of 1%; savings accounts have an annual interest
        rate of 1.2%.

        Returns:
            None
        """
        account_type = self.get_account_type()

        if account_type == "checking":
            interest = self.balance * 0.00083
        else:
            interest = self.balance * 0.001

        self.balance += interest

    def print_statement(self) -> None:
        """
        Prints a message with the account type, account name, account number,
        and the balance.

        Returns:
            None
        """
        obscured_account_number = '****' + self.account_number[4:]
        formatted_balance = f"${self.get_balance_only():.2f}"

        print(f"Account type: {self.get_account_type()}\n"
              f"Account name: {self.full_name}\n"
              f"Account number: {obscured_account_number}\n"
              f"Account balance: {formatted_balance}\n")

    def get_account_number(self):
        return self.account_number


def perform_bank_operations_tina(account: BankAccount) -> None:
    """
    Example 1:
    Perform a series of banking operations on the given account (Tina).

    Args:
        account (BankAccount): The account on which the operations will be performed.

    Returns:
        None
    """
    # Deposit $100,000 into the account
    account.deposit(100000)

    # Print a statement
    print(f"--- {account.full_name}'s initial statement after deposit ---")
    account.print_statement()

    # Add interest to the account
    account.add_interest()

    # Print a statement after adding interest
    print(f"--- {account.full_name}'s statement after adding interest ---")
    account.print_statement()

    # Make a withdrawal of $50
    account.withdraw(50)

    # Print a statement after the withdrawal
    print(f"--- {account.full_name}'s statement after withdrawal ---")
    account.print_statement()


def perform_bank_operations_gene(account: BankAccount) -> None:
    """
    Example 2:
    Perform a series of banking operations on the given account (Gene).

    Args:
        account (BankAccount): The account on which the operations will be performed.

    Returns:
        None
    """
    # Deposit $800,000 into the account
    account.deposit(800000)

    # Print a statement
    print(f"--- {account.full_name}'s initial statement after deposit ---")
    account.print_statement()

    # Add interest to the account
    account.add_interest()

    # Print a statement after adding interest
    print(f"--- {account.full_name}'s statement after adding interest ---")
    account.print_statement()

    # Make a withdrawal of $77
    account.withdraw(77)

    # Print a statement after the withdrawal
    print(f"--- {account.full_name}'s statement after withdrawal ---")
    account.print_statement()


def perform_bank_operations_louise(account: BankAccount) -> None:
    """
    Example 3:
    Perform a series of banking operations on the given account (Louise).

    Args:
        account (BankAccount): The account on which the operations will be performed.

    Returns:
        None
    """
    # Deposit $600,000 into the account
    account.deposit(600000)

    # Print a statement
    print(f"--- {account.full_name}'s initial statement after deposit ---")
    account.print_statement()

    # Add interest to the account
    account.add_interest()

    # Print a statement after adding interest
    print(f"--- {account.full_name}'s statement after adding interest ---")
    account.print_statement()

    # Make a withdrawal of $150
    account.withdraw(150)

    # Print a statement after the withdrawal
    print(f"--- {account.full_name}'s statement after withdrawal ---")
    account.print_statement()


# Create bank accounts
tina_account = BankAccount("Tina Belcher", "checking")
gene_account = BankAccount("Gene Belcher", "checking")
louise_account = BankAccount("Louise Belcher", "savings")

# Perform bank operations for each bank account
print("------------ Example 1 with Tina Belcher ------------")
perform_bank_operations_tina(tina_account)
print("------------ Example 2 with Gene Belcher ------------")
perform_bank_operations_gene(gene_account)
print("------------ Example 3 with Louise Belcher ------------")
perform_bank_operations_louise(louise_account)

# # # # # # # # #  # # # Optional Stretch Challenge # # # # # # # # # # # # #
# Create a list called: bank. Add all of your accounts to bank.
# Write a function that loops over all accounts in the list and calls the
# add_interest method of each.

# Create a list called bank and add interest
bank = [tina_account, gene_account, louise_account]


def add_interest_to_account(accounts: list) -> None:
    """
    Loops over all accounts in the list and calls add_interest method on each.
    Args:
        accounts (list): List of bank account objects.

    Returns:
        None
    """
    for account in accounts:
        if account.get_account_type() == "checking":
            account.add_interest()
        elif account.get_account_type() == "savings":
            account.add_interest()

        print(f"Account name: {account.full_name}\n"
              f"Account type: {account.account_type}\n"
              f"Updated balance is: ${account.get_balance_only():.2f} with interest\n")


print(f"~~~~~~~~~~ Call add_interest_to_account ~~~~~~~~~~")
add_interest_to_account(bank)
