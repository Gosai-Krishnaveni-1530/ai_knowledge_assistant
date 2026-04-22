from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routes.upload import router as upload_router
from routes.query import router as query_router

app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request, "message": "FastAPI is working!"}
    )

app.include_router(upload_router)
app.include_router(query_router)
