from peewee import Model, CharField, DateField
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateField()

    class Meta:
        database = db