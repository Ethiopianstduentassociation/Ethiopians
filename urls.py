from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("apply/", views.apply, name="apply"),
    path("application-received/", views.application_received, name="application_received"),
    path("stories/", views.stories, name="stories"),
    path("stories/<int:pk>/", views.story_detail, name="story_detail"),
    path("donate/", views.donate, name="donate"),
]
