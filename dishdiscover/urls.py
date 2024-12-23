from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('',include('recipe.urls')),
    path('Auth/',include('Auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
