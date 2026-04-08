from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(title="Lab System API")
app.include_router(router)
