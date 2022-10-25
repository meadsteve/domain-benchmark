from typing import Dict

from validation import assert_valid_username, assert_valid_age, assert_valid_email


def parse_data(raw: Dict) -> Dict:
    assert_valid_username(raw["username"])
    assert_valid_age(raw["age"])
    assert_valid_email(raw["email"])
    return dict(
        username=raw["username"],
        age=raw["age"],
        email=raw["email"]
    )
