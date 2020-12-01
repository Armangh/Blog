from django.contrib import admin
from django.urls import path, include

from core.views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', MainPage.as_view(), name="main_page"),
]
