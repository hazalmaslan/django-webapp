from django.urls import path
from . import views


urlpatterns = [
    # /
    path('', views.dashboard, name='dashboard'),

    # /upload/
    path('upload/', views.upload, name='upload'),

    # /virus_total_search/
    path('virus_total_search/', views.virus_search, name='virus_total_search'),

    # /login/
    path('login/', views.login_user, name='login'),

    # /logout/
    path('logout/', views.logout_user, name='logout'),

    # /register/
    path('register/', views.register, name='register'),

    # /detail/
    path('detail/', views.detail, name='detail'),

    # /upload_files/
    path('upload_files/', views.BasicUploadView.as_view(), name='upload_files'),

    # /clear/
    path('clear/', views.clear_database, name='clear_database'),
]

