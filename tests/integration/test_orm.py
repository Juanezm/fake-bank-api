from fakebank.domain import model


def test_create_new_user(session):
    user = model.User()
    session.add(user)
    session.commit()
    users_query = session.query(model.User).all()
    assert user in users_query


def test_create_multiple_user(session):
    user1 = model.User()
    session.add(user1)
    user2 = model.User()
    session.add(user2)
    session.commit()
    users_query = session.query(model.User).all()
    assert user1 in users_query
    assert user2 in users_query


def test_create_user_account(session):
    user = model.User()
    user.add_account()
    session.add(user)
    session.commit()
    users_query = session.query(model.User).all()
    assert user in users_query
