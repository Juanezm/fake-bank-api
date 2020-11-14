
class User:
    """An User of Fake Bank.

    Attributes:
        id: A int representing the user's id.
        accounts: A list of bank accounts for the user.
    """

    def __init__(self):
        self.id = None
        self.accounts = set()

    def add_account(self):
        self.accounts.add(Account(self.id))

    def get_accounts(self):
        return self.accounts


class Account:
    """An Account for Fake Bank.

    Attributes:
        user_id: A string representing the user's id.
        balance: A float representing the total account's balance in GBP.
    """

    def __init__(self, user_id: int):
        self.id = None
        self.user_id = user_id
        self.balance = 0.0

    def update_balance(self, new_balance: float):
        self.balance = new_balance

    def get_balance(self):
        return self.balance
