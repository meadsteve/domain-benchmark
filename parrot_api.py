from typing import Dict

from starlette.status import HTTP_200_OK
from starlite import Starlite,  post


@post("/", status_code=HTTP_200_OK)
def say_back(data: Dict[str, str]) -> Dict[str, str]:
    print(data)
    return data


app = Starlite(route_handlers=[say_back])
