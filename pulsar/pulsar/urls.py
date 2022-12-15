from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += yasg_urls
    urlpatterns += [
        path('', RedirectView.as_view(pattern_name='schema-swagger-ui'))
    ]
