
from django.contrib import admin
from django.urls import path, include

app_name = 'base'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('sign.urls')),
    path('', include('protect.urls')),
]
