import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()

templates = Jinja2Templates("templates")


@router.get("/", include_in_schema=False)
async def index(request: Request):
    # events = await report_service.get_reports()
    # data = {'request': request, 'events': events}
    data = {"request": request}
    return templates.TemplateResponse("home/index.html", data)


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    # TODO: Find out best way to add HTTP Status code
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
