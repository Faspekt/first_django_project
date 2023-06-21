import time


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from users.models import User


class HomePage(ListView):
    """Home page"""

    template_name = "main/home.html"

    def get(self, request):
        self.request.session.set_expiry(0)

        user = self.request.session.get("user", None)
        user_id = self.request.user.id
        data = {"title": "Главная"}

        if user is not None or user_id is None:  # If the user in the session exists

            return render(self.request, self.template_name, data)

        else:  # Creates a user in a new session
            user = get_object_or_404(User, pk=self.request.user.id)

            last_operation_time = self.request.session[
                "last_operation_time"
            ] = time.time()

            self.request.session["user"] = {
                "id": user.pk,
                "username": user.username,
                "avatar": user.avatar.url,
                "is_authenticated": True,
            }
            return render(
                self.request,
                self.template_name,
                {"user": user, "last_operation_time": last_operation_time},
            )


def about_page(request):
    """about page"""
    data = {"about": "О нас"}

    return render(request, "main/about.html", data)


def help_page(request):
    """help page"""
    data = {"help": "Поддержка"}

    return render(request, "main/help.html", data)
