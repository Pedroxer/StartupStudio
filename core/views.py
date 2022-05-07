from django.http import HttpResponse

from core.models import Project
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the core's index.")


def event(request):
    latest_projects_list = Project.objects.all()
    return HttpResponse(
        "This is event placeholder:" + latest_projects_list[0].project_name + " " + latest_projects_list[
            0].project_info)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("NewsFeed:news")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="core/register.html", context={"register_form": form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def logout_view(request):
    logout(request)
    return HttpResponse("You logged out!")

def login_view(request): ##Это все надо переделать через встроенные view
    if request.method == "POST":
        user = authenticate(username='Will', password='hah')
        if user is not None:
            login(request, user)
    form = NewUserForm()
    return render(request=request, template_name="core/login.html", context={"register_form": form})