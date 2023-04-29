from .views import Register
from django.urls import include, path


app_name = "user"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", Register.as_view(), name="register"),
]
