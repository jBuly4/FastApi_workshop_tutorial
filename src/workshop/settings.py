from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'

'''
when instance of settings is created then that class reads env variables and use their values if their name are the 
same as class attributes. after that values are checked, validated and process type convertion
'''

settings = Settings(
        _env_file='.env',  # path to .env file
        _env_file_encoding='utf-8'
)  # will be used in __main__.py
