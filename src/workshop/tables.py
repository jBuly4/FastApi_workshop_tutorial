# file to define tables with alchemy

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# we need user model to create services with registration and authorization
# to simplify - we won't create migrations. just recreate db
class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    password_hash = sa.Column(sa.Text)


class Operation(Base):
    __tablename__ = 'operations'
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)  # nullable means that this field is optional

    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))


'''
creation of test table through python console
from src.workshop.database import engine
from src.workshop.tables import Base

Base.metadata.create_all(engine)
'''
