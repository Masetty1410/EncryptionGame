
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('encrypt', views.encrypt, name='encrypt'),
    path('decrypt', views.decrypt, name='decrypt')
]
