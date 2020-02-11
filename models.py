from peewee import *
from playhouse.postgres_ext import *
import datetime
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

    def serialize(self):
        date = {'date': self.date, 'image': str(self.image), 'license': str(self.license), 'sum': str(self.sum)}
        return date

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.date, self.image, self.license, self.sum)

    def get_all_sales(self):
        sales = Sales.select()
        return sales


def create_tables(db, *args):
    db.connect()
    db.create_tables(*args)
    db.close()

# Simple creation tables
# create_tables(ext_db, [Sales, Licences])


print([_.serialize for _ in Sales().get_all_sales()][:10])

# dir(Licences)
