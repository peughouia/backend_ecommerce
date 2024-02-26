from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()


def inscription(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request, user)
        return redirect('index')

    return render(request, "accounts/inscription.html")


def connexion(request):
    if request.method == "POST":
        # connecter le user
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, "accounts/connexion.html")


def deconnexion(request):
    logout(request)
    return redirect('index')
