from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ai_generator import generate_topics, generate_script

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "topics": None})

@app.post("/", response_class=HTMLResponse)
async def get_ideas(request: Request, niche: str = Form(...)):
    topics = generate_topics(niche)
    return templates.TemplateResponse("index.html", {"request": request, "topics": topics, "niche": niche})

@app.post("/script", response_class=HTMLResponse)
async def get_script(request: Request, title: str = Form(...)):
    script = generate_script(title)
    return templates.TemplateResponse("index.html", {"request": request, "script": script, "title": title})
