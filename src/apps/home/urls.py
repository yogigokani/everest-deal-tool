from django.conf.urls import url
from .views import home


urlpatterns = [
    url(r'^$', view=home, name='index'),
]