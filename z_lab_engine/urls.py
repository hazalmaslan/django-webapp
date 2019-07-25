from django.urls import path
from . import views


urlpatterns = [
    # engine/
    path('', views.dashboard, name='dashboard'),

    # engine/search/
    path('search/', views.search, name='search'),

    # engine/update/
    path('upload/', views.upload, name='upload'),
]
