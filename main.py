import uvicorn
from fastapi import FastAPI
from fastapi.security import HTTPBasic

import src

from src.router.crud import chack2
from src.router.deployments import chack

app = FastAPI()
security = HTTPBasic()

app.include_router(src.router.deployments.router, prefix="/deployments")
app.include_router(src.router.crud.router, prefix="/crud")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    chack()
    chack2()
