# to run app without console
import uvicorn

uvicorn.run(
        'src.workshop.app:app',  # path to app
        reload=True,  # reload server after code upgrade
)