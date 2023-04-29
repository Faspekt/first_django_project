from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm


class Register(View):
    template_name = "registration/user_register.html"

    def get(self, request):
        context = {"form": UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=password)
            user = form.save()
            login(request, user)
            return redirect("main:home")
        context = {"form": form}
        return render(request, self.template_name, context)
