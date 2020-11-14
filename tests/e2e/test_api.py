import requests

from fakebank import config


def test_create_new_user():
    url = config.get_api_url()
    r = requests.post(f'{url}/user')
    assert r.status_code == 200


def test_create_account_for_user():
    url = config.get_api_url()
    data = {'user_id': 1}
    r = requests.post(f'{url}/account', json=data)
    assert r.status_code == 200


def test_update_user_account_balance():
    url = config.get_api_url()
    data = {'user_id': 1, 'account_id': 1, 'balance': 123.45}
    r = requests.put(f'{url}/account', json=data)
    assert r.status_code == 200


def test_get_accounts_for_user(session):
    url = config.get_api_url()
    r = requests.get(f'{url}/accounts/1')
    assert r.status_code == 200
