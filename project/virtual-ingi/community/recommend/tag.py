import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from community.models import Tour

tourList = pd.DataFrame(Tour.objects.values_list('name', 'tag__name'), columns=['name','tag'])
tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index()
tag = pd.DataFrame([('test','바다,문화')], columns=tourList.columns)
tourList = pd.concat([tourList,tag])
print(tourList)

counter_vector = CountVectorizer(ngram_range=(1,3))
c_vector_tags = counter_vector.fit_transform(tourList['tag'])

similarity_tag = cosine_similarity(c_vector_tags, c_vector_tags)
similarity_tag = pd.DataFrame(similarity_tag, index=tourList['name'], columns=tourList['name'])

def get_content_based_collabor(tag):
    tourList = similarity_tag[tag].sort_values(ascending=False)[:20].reset_index()
    tourListVisit = pd.DataFrame(Tour.objects.values_list('name', 'visitCnt'), columns=['name','visit'])
    tourList = tourList.merge(tourListVisit, on="name", how= 'inner')
    tourList.drop(columns=[tag], axis=1, inplace=False)
    print(tourList)

print(get_content_based_collabor('test'))
