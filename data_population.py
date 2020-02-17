import datetime
import random
import math
import pprint
from models import *

SALES_DATA = random.choices([0.36, 2.7, 13.36, 0.44],
                            [68.87,  19.28, 0.37, 11.48], k=8257)
IMAGES_ID = [random.randrange(1000000000, 2000000000) for _ in range(100)]

LICENCES = [{'name': 'Subscription'}, {'name': 'On demand'},
            {'name': 'Enhanced'}, {'name': 'Single & other'}]


def get_downloads_count(avg_downloads, i):
    d = math.ceil(random.gauss(avg_downloads +
                               i * 0.06, avg_downloads * 0.6))
    downloads_per_day = d if d > 0 else 0
    return downloads_per_day


def get_lecense_type(price):
    license_type = 1 if price == 0.36 else 2 if price == 2.7 else random.choices(
        [3, 4], [0.37, 11.48], k=1)[0]
    return license_type


def generate_stock_data(sales_data, images_id):
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date.today()
    time_delta = (end_date - start_date).days
    avg_downloads = 7.44
    stock_data = []
    end_of_set = 0
    for i in range(time_delta):
        date = start_date + datetime.timedelta(days=i)
        downloads_per_day = get_downloads_count(avg_downloads, i)
        end_of_set += downloads_per_day
        start_of_set = end_of_set - downloads_per_day
        # print("{} - {}".format(start_of_set, end_of_set))
        price_set = sales_data[start_of_set:end_of_set]
        for price in price_set:
            day = {'date': date, 'image': random.choice(images_id),
                   'license': get_lecense_type(price), 'sum': price}
            stock_data.append(day)
    return stock_data

# generate_stock_data(SALES_DATA, IMAGES_ID)
# pprint.pprint(generate_stock_data(SALES_DATA, IMAGES_ID), indent=2, width=160)


# Licences.insert_many(LICENCES).execute()
Sales.insert_many(generate_stock_data(SALES_DATA, IMAGES_ID)).execute()
