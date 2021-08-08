from django.urls import path

from accountapp.views.main import main_slogan, result

#from accountapp.views.make_slogan import result_slogan


app_name = "accountapp"

urlpatterns = [
    # account/main_slogan
    path('index/', main_slogan, name="index"),  # url, 연결할 view 함수명, name
    path('result_slogan/', result, name="result_slogan"),
]