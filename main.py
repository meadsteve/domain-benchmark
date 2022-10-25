import os

from domain import parse_data as domain_parse_data
from plain import parse_data as plain_parse_data

USE_DOMAIN_OBJECTS = bool(int(os.environ.get('USE_DOMAIN_OBJECTS', '0')))

parse_data = domain_parse_data if USE_DOMAIN_OBJECTS else plain_parse_data

data = {
    "username": "meadsteve",
    "age": 38,
    "email": "hello@hello.hello"
}
parsed_data = parse_data(data)

print(parsed_data)
