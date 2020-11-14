from fakebank import config
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fakebank.adapters import repository
from fakebank.adapters.orm import metadata, start_mappers

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


start_mappers()
engine = create_engine(config.get_postgres_uri())
get_session = sessionmaker(bind=engine)
metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class User(BaseModel):
    user_id: int


class Account(BaseModel):
    user_id: int
    account_id: int
    balance: float


@app.post("/user")
async def create_new_user():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    user = repo.add_user()
    return jsonable_encoder({'user_id': user.id})


@app.post("/account")
async def create_account_for_user(user: User):
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    account_id = repo.add_account_for_user(user_id=user.user_id)
    return jsonable_encoder({'account_id': account_id})


@app.put("/account")
async def update_user_account_balance(account: Account):
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    account = repo.update_account_for_user(
        user_id=account.user_id,
        account_id=account.account_id,
        new_balance=account.balance
    )
    return jsonable_encoder({'account_id': account.id})


@app.get("/accounts/{user_id}")
async def get_accounts_for_user(user_id: int):
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    accounts = repo.get_accounts_from_user(user_id)
    if not accounts:
        raise HTTPException(status_code=404, detail="No accounts not found for this user")
    return jsonable_encoder(accounts)
