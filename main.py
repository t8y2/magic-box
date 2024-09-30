import uvicorn

from pathlib import Path
from core.config import settings
from core.register import register_app

app = register_app()

if __name__ == '__main__':
    uvicorn.run(
        app=f'{Path(__file__).stem}:app',
        host=settings.UVICORN_HOST,
        port=settings.UVICORN_PORT,
        reload=settings.UVICORN_RELOAD,
        access_log=False
    )
