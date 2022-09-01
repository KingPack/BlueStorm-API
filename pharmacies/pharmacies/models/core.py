from ..ext.database2 import Base

from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String, DateTime

from marshmallow import Schema, fields


class PatientsModel(Base):

    __tablename__ = 'PATIENTS'

    UUID = Column(String, primary_key=True)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    DATE_OF_BIRTH = Column(DateTime)


class PatientsSchema(Schema):

    UUID = fields.String()
    FIRST_NAME = fields.String()
    LAST_NAME = fields.String()
    DATE_OF_BIRTH = fields.DateTime()


class PharmaciesModel(Base):

    __tablename__ = 'PHARMACIES'

    uuid = Column(String, primary_key=True)
    name = ''
    city = ''


class PharmaciesSchema(Schema):

    uuid = fields.String()
    name = fields.String()
    city = fields.String()


class UsersModel(Base):

    __tablename__ = 'users'

    UUID = Column(String, primary_key=True)
    USERNAME = Column(String)


class UsersSchema(Schema):

    uuid = fields.String()
    username = fields.String()
    password = fields.String()
