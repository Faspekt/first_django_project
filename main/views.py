from django.shortcuts import render



def home(request):
    data = {
        "title": "Главная",
    }
    return render(request, "main/home.html", data)


def about(request):
    data = {
        "about": "О нас"
    }
    return render(request, "main/about.html", data)


def help(request):
    data = {
        "help": "Поддержка"
    }
    return render(request, "main/help.html", data)

