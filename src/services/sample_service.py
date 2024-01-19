from typing import Optional


async def hello(name: Optional[str] = None):
    if name:
        return {"message": f"Hello {name}!"}
    return {"message": "Hello World!"}
