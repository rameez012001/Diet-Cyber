from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ctapp/', include('ctapp.urls')),
    path('admin/', admin.site.urls),
] 