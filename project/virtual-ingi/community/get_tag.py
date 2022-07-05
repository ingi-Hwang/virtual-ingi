from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import csv
from community.models import Tour
from community.tag_crawling import get_tour_tag

# Create your tests here.
all = Tour.objects.all()

tagAll = list()

for index in all:
    tourName = index.__str__()
    print(tourName)
    tag = get_tour_tag(tourName)
    tagAll.append(tag)

print("done")

with open("output2.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(tagAll)