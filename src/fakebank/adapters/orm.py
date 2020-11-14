from sqlalchemy import Table, Integer, Column, ForeignKey, Float, MetaData
from sqlalchemy.orm import mapper, relationship

from fakebank.domain import model

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True)
)

accounts = Table(
    'accounts', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('balance', Float)
)


def start_mappers():
    accounts_mapper = mapper(model.Account, accounts)
    mapper(model.User, users, properties={
        'accounts': relationship(
            accounts_mapper,
            collection_class=set,
        )
    })
