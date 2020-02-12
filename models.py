import datetime
from peewee import *
from playhouse.postgres_ext import *
# Connect to a Postgres database.
ext_db = PostgresqlExtDatabase('stockstat', user='pavelskrytski')


class BaseExtModel(Model):

    class Meta:
        database = ext_db


class Licences(BaseExtModel):
    name = TextField(unique=True)


class Sales(BaseExtModel):
    date = DateField(default=datetime.date.today())
    image = IntegerField()
    license = ForeignKeyField(Licences, backref='license')
    sum = DecimalField(max_digits=5, decimal_places=2)


def create_tables(db, *args):
    db.connect()
    db.create_tables(*args)
    db.close()

# Simple creation tables
# create_tables(ext_db, [Sales, Licences])
