from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def main_profile(request):
    return render(request, 'MyProfile/main_profile.html')

# Create your views here.
