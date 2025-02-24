from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    # path("events/", views.event_list, name="event-list"),
    # path("events/<int:id>/", views.event_detail, name="event-detail"),
]
