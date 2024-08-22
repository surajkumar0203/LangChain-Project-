from django.contrib import admin
from django.urls import path,include
from myapp.views import index
urlpatterns = [
    path('',index.as_view(),name="index")
]