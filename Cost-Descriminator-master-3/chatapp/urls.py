from django.conf.urls import url
from chatapp import views
from django.views.generic.base import RedirectView
urlpatterns=[
    url(r'^api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),
    
]