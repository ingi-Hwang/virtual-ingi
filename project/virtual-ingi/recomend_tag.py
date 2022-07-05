import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from community.models import *


d3 = Input.objects.get(id=42) # id=32 데이터들
s=""
for i in range(d3.tag.count()):
    s += str(d3.tag.all()[i])
    if i != d3.tag.count()-1:
        s += " "

tourList = pd.DataFrame(Tour.objects.values_list('name', 'tag__name'), columns=['name','tag'])
tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index()
tag = pd.DataFrame([('test',s)], columns=tourList.columns)
tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index()

tourList = pd.concat([tourList,tag])

counter_vector = CountVectorizer(ngram_range=(1,3))
c_vector_tags = counter_vector.fit_transform(tourList['tag'])

similarity_tag = cosine_similarity(c_vector_tags, c_vector_tags)
similarity_tag = pd.DataFrame(similarity_tag, index=tourList['name'], columns=tourList['name'])
# print(similarity_tag)

def get_content_based_collabor(tag):
    tourList = similarity_tag[tag].sort_values(ascending=False)[:20].reset_index()
    tourListVisit = pd.DataFrame(Tour.objects.values_list('name', 'visitCnt', 'tourLatitude', 'tourLongitude'), columns=['name','visit','latitude','longitude'])
    tourList = tourList.merge(tourListVisit, on="name", how= 'inner')
    tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)
    print(tourList,'ss1')

    tourList = tourList.sort_values(by=[tourList.columns[1],tourList.columns[3],tourList.columns[4]], ascending=False)[:10]
    tourList.drop(tourList.columns[[3,4]], axis='columns')
    print(tourList,'ss1')

    tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)
    row_1 = tourList.iloc[0]
    first=row_1[0]
    print(row_1)
    print(first)
    tourList.drop(columns=[tag], axis=1, inplace=False)

    print(tourList,'ss')

print(get_content_based_collabor('test'),"s")
