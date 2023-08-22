from fastapi import FastAPI
from routers import image_router

app = FastAPI()

app.include_router(image_router.router)

@app.get('/')
def read_root():
    return {'Hello':'World'}