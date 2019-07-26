from django.urls import path
from . import views

# Add url patterns of the newly added sites to the z_lab_engine app

urlpatterns = [
    # /
    path('', views.dashboard, name='dashboard'),

    # /search/
    path('search/', views.search, name='search'),

    # /upload/
    path('upload/', views.upload, name='upload'),

    # /virus_total_search/
    path('virus_total_search/', views.search, name='virus_total_search'),

]

