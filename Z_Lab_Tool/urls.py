from django.contrib import admin
from django.urls import path, include

# Do not add url patterns related to z_lab_engine here, add them to z_lab_engine/urls.py
# Add only new app url patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('z_lab_engine.urls')),
]
