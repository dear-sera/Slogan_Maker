import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from accountapp.views.ko_slogan import process, ko_api, differ, extraction
from accountapp.views.en_slogan import enslogan
from accountapp.models import post


def main_slogan(request):
    #request = json.loads(request.body)
    # sim = request['sim']
    # post = post(select = request['select'],
    #             info = request['info'],
    #             sim = int(sim))
    return render(request, 'accountapp/index.html')



def result(request):
    select = request.POST.get("select", None)
    info = request.POST.get("info", None)
    sim = request.POST.get("sim", None)
    sim = int(sim)
    if select == 'ko_slogan':
        text = process(info, sim)
        slogan_list = ko_api(text)
        kor_list = differ(slogan_list)
        total_slogan = extraction(kor_list, sim)
        context = {'slogans': total_slogan, 'select': select}
        # print(total_slogan)
        # print(type(total_slogan))
    elif select == 'en_slogan':
        slogans = enslogan(info)
        context = {'slogans': slogans, 'select': select}
    # else:   'model_slogan'
    #     slogans = sloan(info)
    #     context = {'slogans': slogans, 'select': select}



    return render(request, 'accountapp/result_slogan.html', context=context)




