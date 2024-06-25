from fastapi import FastAPI
from fast_api_app.controllers import addition_controller

app = FastAPI()

app.include_router(addition_controller.router)
