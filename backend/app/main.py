from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .website_generator import WebsiteGenerator

app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WebsiteRequest(BaseModel):
    theme: str
    features: list[str]
    colors: list[str]

generator = WebsiteGenerator()

@app.post("/generate")
async def generate_website(request: WebsiteRequest):
    prompt = f"""
    Create a website with the following details:
    Theme: {request.theme}
    Features: {', '.join(request.features)}
    Colors: {', '.join(request.colors)}
    
    Generate HTML, CSS, and JavaScript code for this website.
    
    HTML:
    """
    
    generated_code = generator.generate_code(prompt)
    return {"code": generated_code}