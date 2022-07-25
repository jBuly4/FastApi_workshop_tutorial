from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'
    # for services/auth.py we need to decode secret and algorithm from payload. so we need this fields
    jwt_secret: str  # for this field we can use from secrets import token_urlsafe token_urlsafe(32) and save it in
    # .env file
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600

'''
when instance of settings is created then that class reads env variables and use their values if their name are the 
same as class attributes. after that values are checked, validated and process type conversion

for jwt we need python-jose
for hashing passwords we need passlib[bcrypt]
'''

settings = Settings(
        _env_file='.env',  # path to .env file
        _env_file_encoding='utf-8'
)  # will be used in __main__.py
