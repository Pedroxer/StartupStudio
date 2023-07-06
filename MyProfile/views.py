from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def main_profile(request):
    return render(request, 'MyProfile/main_profile.html')
    #return HttpResponse('<h2>Проверка</h2>')


def create(request):
    
    return render(request, 'MyProfile/main_profile.html')



# Create your views here.
