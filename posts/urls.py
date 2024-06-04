from django.urls import path
from . import views

urlpatterns = [
    path("", views.Posts.as_view()),
    path("<int:id>/", views.PostDetail.as_view())
]