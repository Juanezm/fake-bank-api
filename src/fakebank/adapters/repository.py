import abc
from typing import List, Set

from fakebank.domain import model
from sqlalchemy.orm.exc import NoResultFound


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self) -> model.User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_account_for_user(self, user_id: int) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self) -> List[model.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_accounts_from_user(self, user_id: int) -> Set[model.Account]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_account_for_user(self,
                                user_id: int,
                                account_id: int,
                                new_balance: float) -> model.Account:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add_user(self):
        user = model.User()
        self.session.add(user)
        self.session.commit()
        return user

    def add_account_for_user(self, user_id):
        self.session.add(model.Account(user_id))
        total_number_user_accounts = self.session.query(model.Account).filter(model.Account.user_id == user_id).count()
        self.session.commit()
        return total_number_user_accounts

    def get_users(self):
        return self.session.query(model.User).all()

    def get_accounts_from_user(self, user_id):
        return set(self.session.query(model.Account).filter(model.Account.user_id == user_id).all())

    def update_account_for_user(self, user_id, account_id, new_balance):
        try:
            account = self.session.query(model.Account). \
                filter(model.Account.user_id == user_id). \
                filter(model.Account.id == account_id).one()

            account.update_balance(new_balance=new_balance)
            self.session.commit()

        except NoResultFound:
            account = None

        return account
