from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="ehome"),
    path('/News', views.News, name="News"),
    path('/feedback', views.Feedback, name="feedback"),
    path('/partail', views.partail, name="partail"),
]