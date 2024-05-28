from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("", include("main.urls")),
    path("", include("users.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
