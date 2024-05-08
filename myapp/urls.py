from django.urls import path
from .views import MyModelListView
from explorer.views import explorer

urlpatterns = [
    path('data/', MyModelListView.as_view(), name='data-list'),
    path('explorer/', explorer, name='explorer'),
]