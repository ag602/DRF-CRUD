"""Boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DRF - CRUD",
      default_version='v1',
      description="Hi! To test the APIs see the below documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="akul.gupta602@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
router = routers.DefaultRouter()


from core import urls
urlpatterns = [
    path(r'^admin', admin.site.urls),
    path('', include('core.urls')),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/api.json/$', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger/$', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    # This is not suitable for production use! For some common deployment strategies, see
    # https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
