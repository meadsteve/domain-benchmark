from typing import Optional


def assert_valid_username(value: Optional[str]):
    if not value:
        raise RuntimeError("Username can not be empty")
    if len(value) > 100:
        raise RuntimeError("For some reason usernames can't be longer than 100 chars")


def assert_valid_age(value):
    if not value:
        raise RuntimeError("Age can not be empty")
    value = int(value)
    if value < 0:
        raise RuntimeError("You must have been born. Please wait...")
    if value > 200:
        raise RuntimeError("No Human has yet lived to 200. Please contact the record books")


def assert_valid_email(value):
    # Note: These are not really serious checks for email.
    #       Please don't copy this
    if not value:
        raise RuntimeError("Email can not be empty")
    if "@" not in value:
        raise RuntimeError("Where's the @?")
    if value.count("@") > 1:
        raise RuntimeError("Too much @")
    if "." not in value:
        raise RuntimeError("We require a dot - though technically emails don't need this")
