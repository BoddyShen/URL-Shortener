from django.urls import path
from .views import shorten_url, redirect_url

# urls -> respond by specific view, name can be used to replace this url in views and templates
urlpatterns = [
    path('', shorten_url, name='shorten'),
    path('<str:short_url>/', redirect_url, name='redirect'),
]

# <str:short_url>/
# a URL pattern with a string parameter <str:short_url>/,
# which means that it will match any URL that has a string after the root URL.
