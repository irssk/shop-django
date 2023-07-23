from django.contrib import admin
from django.urls import path, include

from app.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns))
]
