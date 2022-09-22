from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld', views.index),
] + static(settings.STATICFILES_DIRS, document_root=settings.STATIC_ROOT)
