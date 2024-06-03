from django.conf import settings
from django.contrib import admin
from django.urls import include, path

{% if cookiecutter.include_drf_spectacular == 'yes' %}
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
{% endif %}


# Collection of URLs related to API (V2)
apiv2patterns = [
    {% if cookiecutter.include_drf_spectacular == 'yes' %}
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redocs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    {% endif %}

    path("auth/", include("authmod.urls")),
    path("users/", include("accounts.urls")),
]

# Collection of common URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(apiv2patterns)),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
