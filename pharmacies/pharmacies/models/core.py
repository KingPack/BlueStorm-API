from ..ext.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, String, DateTime, Text
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

    UUID = Column(String, primary_key=True)
    NAME = Column(String)
    CITY = Column(String)


class PharmaciesSchema(Schema):

    UUID = fields.String()
    NAME = fields.String()
    CITY = fields.String()


class UsersModel(Base):

    __tablename__ = 'users'

    UUID = Column(String, primary_key=True)
    USERNAME = Column(Text)
    PASSWORD = Column(String)


class UsersSchema(Schema):

    UUID = fields.String()
    USERNAME = fields.String()
    PASSWORD = fields.String()


class TransactionsModel(Base):

    __tablename__ = 'TRANSACTIONS'

    UUID = Column(String, primary_key=True)
    PATIENT_UUID = Column(String, ForeignKey("PatientsModel.UIID"))
    PHARMACY_UUID = Column(String, ForeignKey("PharmaciesModel.UIID"))
    AMOUNT = Column(Float)
    TIMESTAMP = Column(DateTime)


class TransactionsSchema(Schema):

    UUID = fields.String()
    PATIENT_UUID = fields.String()
    PHARMACY_UUID = fields.String()
    AMOUNT = fields.Float()
    TIMESTAMP = fields.String()
