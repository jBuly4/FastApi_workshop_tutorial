# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get('/')
# def root():
#     return {'message': 'Hello!'}

#  let's reorganize our code
#  api packet for our handlers
#  services packet for business logic
#  models packet for description of data models
#  settings.py as config file
#  in api __init__ we need to create main router

from fastapi import FastAPI
from .api import router

app = FastAPI()
app.include_router(router)
