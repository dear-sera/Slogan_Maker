import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accountapp.views.ko_slogan import process, ko_api, differ, extraction
from accountapp.views.en_slogan import enslogan
from accountapp.views.ko_model import koslogan
from accountapp.models import post
from django.core.paginator import Paginator


def main_slogan(request):
    if request.method == "POST":
        return render(request, "accountapp/index.html")
    else:
        return render(request, "accountapp/index.html")

def loading_view(request):
    request.session["select"] = request.POST.get("select", None)
    request.session["info"] = request.POST.get("info", None)
    request.session["sim"] = request.POST.get("sim", None)
    return render(request, "accountapp/loading.html")

def result(request):
    select = request.session["select"]
    info = request.session["info"]
    sim = request.session["sim"]
    sim = int(sim)
    if select == "ko_slogan":
        text = process(info, sim)
        slogan_list = ko_api(text)
        kor_list = differ(slogan_list)
        total_slogan = extraction(kor_list, sim)
        context = {"slogans": total_slogan, "select": select}
    elif select == "en_slogan":
        slogans = enslogan(info)
        context = {"slogans": slogans, "select": select}
    else:
        slogans = koslogan(info)
        context = {'slogans': slogans, 'select': select}

    return render(request, "accountapp/result_slogan.html", context=context)


def show(request):
    value = request.POST.getlist("checkvalue")
    # paginator = Paginator(value, 1)
    # page = request.GET.get("page")
    # posts = paginator.get_page(page)
    context = {"slogans": value}

    return render(request, "accountapp/show.html", context=context)


# class show_list(ListView):
#     context_object_name = 'value'
#     template_name = 'accoutapp/show.html'
#     paginate_by = 1  #페이지 별 25객체를 보여준다
