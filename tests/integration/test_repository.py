from fakebank.domain import model
from fakebank.adapters import repository
import random


def add_random_users(session):
    users = list()

    for u in range(0, random.randint(1, 10)):
        user = model.User()
        for a in range(0, random.randint(1, 5)):
            user.add_account()
        users.append(user)
        session.add(user)

    session.commit()
    return users


def test_repository_can_add_user(session):
    repo = repository.SqlAlchemyRepository(session)
    user = repo.add_user()

    users = session.query(model.User).all()
    assert user in users


def test_repository_can_get_users(session):
    created_users = add_random_users(session)

    repo = repository.SqlAlchemyRepository(session)
    users = repo.get_users()

    assert created_users == users


def test_get_accounts_from_user(session):
    created_users = add_random_users(session)
    random_user = random.choice(created_users)

    repo = repository.SqlAlchemyRepository(session)
    accounts = repo.get_accounts_from_user(random_user.id)

    assert random_user.get_accounts() == accounts


def test_update_account_for_user(session):
    created_users = add_random_users(session)

    random_user = random.choice(created_users)
    random_account = random.choice(list(random_user.get_accounts()))
    random_balance = round(random.uniform(0, 2000), 2)

    repo = repository.SqlAlchemyRepository(session)
    account = repo.update_account_for_user(random_user.id, random_account.id, random_balance)

    assert account.balance == random_balance


def test_no_update_non_existing_account_for_user(session):
    session.add(model.User())
    random_balance = round(random.uniform(0, 2000), 2)

    repo = repository.SqlAlchemyRepository(session)
    account = repo.update_account_for_user(1, 2, random_balance)

    assert not account


def test_user_can_add_account(session):
    created_users = add_random_users(session)
    random_user = random.choice(created_users)

    repo = repository.SqlAlchemyRepository(session)
    number_user_accounts = repo.add_account_for_user(user_id=random_user.id)

    user_accounts = set(session.query(model.Account).filter(model.Account.user_id == random_user.id).all())
    assert number_user_accounts == len(user_accounts)
