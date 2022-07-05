import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from community.models import Stay #무조건 os밑으로


with open('community/data/sleep.csv', encoding='CP949') as csv_file_sub_categories: #오픈파일 위치
    rows = csv.reader(csv_file_sub_categories)
    print(rows)
    next(rows, None)
    for row in rows:
        Stay.objects.create(
            name = row[0], #모델 이름에 맞추어 적기
            stayLatitude = row[1],
            stayLognitude = row[2]
        )
        print(row)