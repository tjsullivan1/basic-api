from typing import Optional


def make_json_string(sample_string):
    return f'{{"message": "{sample_string}"}}'


async def hello(name: Optional[str] = None):
    if name:
        return make_json_string("Hello {name}!")
    return make_json_string("Hello World!")
