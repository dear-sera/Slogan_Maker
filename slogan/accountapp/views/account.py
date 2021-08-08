from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import main_slogan
from django.utils import timezone
from django.views.generic import CreateView



# class AccountCreateView(CreateView):
#     model = User # 장고에서 기본 제공해주는 모델
#     form_class = 