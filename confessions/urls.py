from django.urls import path, include
#from .views import article_list, article_detail
from .views import ConfessionDetail, ConfessionList
urlpatterns = [

    #path('', article_list ),
    #path('<int:pk>/', article_detail),
    path('', ConfessionList.as_view()),
    path('<int:pk>/', ConfessionDetail.as_view()),
    ]