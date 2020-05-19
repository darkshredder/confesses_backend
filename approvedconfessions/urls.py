from django.urls import path, include
from .views import ApprovedconfessionsList

urlpatterns = [
    path('', ApprovedconfessionsList.as_view()),
    
]
