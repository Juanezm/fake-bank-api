from fakebank.domain.model import User, Account


def test_user_can_add_account():
    usr = User()
    usr.add_account()
    assert len(usr.get_accounts()) is 1


def test_account_can_update_and_get_balance():
    account = Account(1)
    updated_balance = 123.45
    account.update_balance(updated_balance)
    assert account.get_balance() is updated_balance
