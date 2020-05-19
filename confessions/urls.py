from django.urls import path, include
#from .views import article_list, article_detail
from .views import  ConfessionList
urlpatterns = [

    path('', ConfessionList.as_view()),
    ]