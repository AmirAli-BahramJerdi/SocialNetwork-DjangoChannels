from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', include('home.urls', namespace='home')),
    path('account/', include('account.urls', namespace='account')),
]
