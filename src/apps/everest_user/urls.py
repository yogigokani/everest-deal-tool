"""URL's for esf_us forms."""

from django.conf.urls import url
from .views import everest_login, everest_logout


urlpatterns = [
    url(r'^login/$', view=everest_login, name='login'),
    url(r'^logout/$', view=everest_logout, name='logout'),
]
