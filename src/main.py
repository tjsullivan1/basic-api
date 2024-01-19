from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import sample_api
from views import home

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(sample_api.router)


if __name__ == "__main__":
    configure()
#  uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
