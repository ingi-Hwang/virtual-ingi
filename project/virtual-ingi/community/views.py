from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

#밑에 부분이 추천
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.
#
def Home(request):
    return render(request, 'community/home.html')


def Date(request):
    if request.method == 'POST':
        # db 저장할때
        user = Input()
        user.startperiod = request.POST['date']  # input에 name으로 받아야 값을 받을수 있음
        user.endperiod = request.POST['date2']
        user.startime = request.POST['time']
        user.area = request.POST['local']
        tag = request.POST.getlist('tag[]')
        # user.tag3 = tag

        # 추천시스템
        print(len(tag))
        s = ""
        for i in range(len(tag)):
            s += str(tag[i])
            if i != len(tag) - 1:
                s += " "
        print(s)

        tourList = pd.DataFrame(Tour.objects.values_list('name', 'tag__name'), columns=['name', 'tag'])
        tourList = tourList.groupby(['name'])['tag'].apply(','.join).reset_index()
        tag = pd.DataFrame([('test', s)], columns=tourList.columns)
        tourList = pd.concat([tourList, tag])

        counter_vector = CountVectorizer(ngram_range=(1, 3))
        c_vector_tags = counter_vector.fit_transform(tourList['tag'])

        similarity_tag = cosine_similarity(c_vector_tags, c_vector_tags)
        similarity_tag = pd.DataFrame(similarity_tag, index=tourList['name'], columns=tourList['name'])

        def get_content_based_collabor(tag):
            tourList = similarity_tag[tag].sort_values(ascending=False)[:20].reset_index()
            tourListVisit = pd.DataFrame(Tour.objects.values_list('name', 'visitCnt', 'tourLatitude', 'tourLongitude'),
                                         columns=['name', 'visit', 'latitude', 'longitude'])
            tourList = tourList.merge(tourListVisit, on="name", how='inner')
            tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)
            tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[3], tourList.columns[4]],
                                            ascending=False)[:10]
            tourList.drop(tourList.columns[[3, 4]], axis='columns')

            tourList = tourList.sort_values(by=[tourList.columns[1], tourList.columns[2]], ascending=False)
            row_1 = tourList.iloc[0]
            first = row_1[0]
            print(row_1)
            print(first)
            tourList.drop(columns=[tag], axis=1, inplace=False)

            print(tourList, 'ss')

        print(get_content_based_collabor('test'), "s")

        return render(request, 'community/date.html', {'data': user})

    else:
        user = Users.objects.all()

        return render(request, 'community/date.html', {'data': user})