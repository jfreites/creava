from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("", include("landing.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
