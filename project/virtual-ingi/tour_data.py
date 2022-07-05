import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from community.models import Tour #무조건 os밑으로


with open('community/data/tour.csv', encoding='utf-8') as csv_file_sub_categories: #오픈파일 위치
    rows = csv.reader(csv_file_sub_categories)
    print(rows)
    next(rows, None)
    for row in rows:
        Tour.objects.create(
            tour_name = row[1], #모델 이름에 맞추어 적기
            latitude = row[2],
            hardness = row[3],
            img_url = row[4]
        )
        print(row)