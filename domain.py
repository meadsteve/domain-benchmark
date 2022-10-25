from typing import Dict

from validation import assert_valid_username, assert_valid_age, assert_valid_email


class Username(str):
    def __init__(self, value):
        assert_valid_username(value)


class Age(int):
    def __init__(self, value):
        assert_valid_age(value)


class EmailAddress(str):
    def __init__(self, value):
        assert_valid_email(value)


class Person:
    username: Username
    age: Age
    email: EmailAddress

    def __init__(self, username: Username, age: Age, email: EmailAddress):
        self.username = username
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.username} - {self.age} - {self.email}"

    def __getitem__(self, item):
        # This method exists so we can use the Person class as a drop-in replacement
        # for the plain dictionary
        if item not in ["username", "email", "age"]:
            raise KeyError("That is not a valid property")
        return self.__dict__[item]


def parse_data(raw: Dict) -> Person:
    return Person(
        username=Username(raw["username"]),
        age=Age(raw["age"]),
        email=EmailAddress(raw["email"])
    )
