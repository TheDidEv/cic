# this urls.py will be imported on cicback/urls.py
from django.urls import path
# from .views import ArrayView
from . import views

urlpatterns = [
    path('getArray', views.getArr),
    path('postArray', views.postArr),
    path('bubbleSort', views.bubbleSort),
    path('insertionSort', views.insertionSort)
]
