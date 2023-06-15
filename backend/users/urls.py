from django.urls import path
from .views import *

urlpatterns = [
    path("login", UserLoginView.as_view()),
    path("logout", UserLogoutView.as_view()),
    path("student/", EtudiantView.as_view()),
    path("student/<str:id>", EtudiantView.as_view()),
    # lecturer route
    path("lecturer/", LecturerView.as_view()),
    path("lecturer/<str:id>", LecturerView.as_view()),
]