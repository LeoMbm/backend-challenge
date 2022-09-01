import csv
import os
from logs.models import Logs, Countries


def run():
    file = open('/home/lordbitches/PycharmProjects/IPview/logs.csv')
    read_file = csv.reader(file)
    count = 1
    for r in read_file:
        if count == 1:
            pass
        else:
            Logs.objects.create(id=r[0], ip=r[1],country=r[2], date=r[3])
            # Countries.objects.create(country=r[2], ip_id=r[0])
        count = count + 1
