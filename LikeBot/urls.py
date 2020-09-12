from django.contrib import admin
from django.urls import path
from likemebot.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name="home"),
    path('test',Test, name="test"),
]
