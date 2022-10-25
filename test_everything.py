import os

import pytest

from domain import parse_data as domain_parse_data
from plain import parse_data as plain_parse_data

USE_DOMAIN_OBJECTS = bool(int(os.environ.get('USE_DOMAIN_OBJECTS', '0')))

parse_data = domain_parse_data if USE_DOMAIN_OBJECTS else plain_parse_data


def _parse_a_bunch_of_happy_users():
    raw_users_data = [
        {"username": "meadsteve", "age": 38, "email": "hello@hello.hello"},
        {"username": "a", "age": 1, "email": "2@a.com"},
        {"username": "really-long-name-with-dashes", "age": 100, "email": "old@web.com"},
    ]
    for raw_user in raw_users_data:
        parse_data(raw_user)


@pytest.mark.happy
def test_valid_users_get_parsed_and_no_data_is_lost(benchmark):
    benchmark(_parse_a_bunch_of_happy_users)


def _exception_raising_parse(raw_user_data):
    try:
        parse_data(raw_user_data)
    except Exception:
        return True
    return False


def _parse_a_bunch_of_sad_users():
    raw_users_data = [
        {"username": "", "age": 38, "email": "hello@hello.hello"},
        {"username": "a", "age": 0, "email": "2@a.com"},
        {"username": "really-long-name-with-dashes", "age": 300, "email": "old@web.com"},
        {"username": "really-long-name-with-dashes", "age": None, "email": "old@web.com"},
        {"username": "a", "age": 22, "email": "yes"},
        {"username": "a", "age": "old", "email": "yes"},
    ]
    for raw_user in raw_users_data:
        _exception_raising_parse(raw_user)


@pytest.mark.sad
def test_invalid_user_data_raises_an_exception(benchmark):
    benchmark(_parse_a_bunch_of_sad_users)
