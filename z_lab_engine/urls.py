from django.urls import path
from . import views


urlpatterns = [
    # engine/
    path('', views.dashboard, name='dashboard'),

    # engine/search/
    path('search/', views.search, name='search'),

    # engine/update/
    path('upload/', views.upload, name='upload'),

    # engine/virus_total_search
    path('virus_total_search/', views.search, name='virus_total_search'),
]

