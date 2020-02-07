from peewee import *
from playhouse.postgres_ext import *
import datetime
# Connect to a Postgres database.
ext_db = PostgresqlExtDatabase('stockstat', user='pavelskrytski')

class BaseExtModel(Model):
    class Meta:
        database = ext_db

class Licences(BaseExtModel):
    name = TextField()

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


data_sales = [
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23},
    {'date': datetime.date.today(), 'image': 1000000000, 'license': 1, 'sum': 10.23}
]

data_licences = [
    {'name': 'Subscription'},
    {'name': 'OnDemand'}
]

Licences.insert_many(data_licences).execute()
Sales.insert_many(data_sales).execute()

