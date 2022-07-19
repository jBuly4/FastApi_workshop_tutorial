# to run app without console
import uvicorn

from .settings import settings

uvicorn.run(
        'src.workshop.app:app',  # path to app
        host=settings.server_host,
        port=settings.server_port,
        reload=True,  # reload server after code upgrade
)