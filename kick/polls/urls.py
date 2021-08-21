from django.urls import path
from polls import views

urlpatterns = patterns(
    '',
    url(r'^$', 'views.index', name='index')
)


