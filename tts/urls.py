from django.urls import path
from .views import home, synthesize

urlpatterns = [
    path("", home, name="home"),
    path("synthesize/", synthesize, name="synthesize"),
]
