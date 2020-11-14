# FakeBank API

## Introduction

This application provides an user interface through a REST API to administrate the users and bank accounts of fakeBank.

Each user can have none or multiple bank accounts, and these bank accounts have a balance given in GBP.

The requirements are:
- Create new user
- Create account for user given their ID
- Update account balance
- Return all accounts for an user


It has been built on Python using the following libraries:
- FastAPI
- SQLAlchemy
- PyTest

## Deployment

Follow the Makefile file for instructions or:

Deploy the app using docker compose

```docker
docker-compose up -d app
```

Open http://localhost:8000/docs
