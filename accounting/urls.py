from django.contrib import admin
from django.urls import path, include
from .views import AdminTokenCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("journal.urls")),
    path('admin/token/', AdminTokenCreateView.as_view(), name='admin-token-create'),
]
