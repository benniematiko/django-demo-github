
from django.urls import path
from .views import home_page_views

urlpatterns = [
    path('', home_page_views, name='HomePage'),
   
]
