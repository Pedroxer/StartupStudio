from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from MyProfile.models import Profile
from UserSystem.models import CustomUser
from django.core.exceptions import PermissionDenied

@login_required
def main_profile(request):
    try:
        user_profile = Profile.objects.get(email=request.user.email)
    except Profile.DoesNotExist:
        return redirect('MyProfile/ent')
    ctx = {'first_name':user_profile.firstname,
    'last_name':user_profile.lastname,
    'sername':user_profile.sername,
    'birth_date':user_profile.birth_date,
    'email':user_profile.email,
    'skils':user_profile.skills,
    'extrainfo':user_profile.extrainfo,
    'adres':user_profile.contact_info,
    'direction':user_profile.direction,
    'graduate_date':user_profile.graduate_date,
    'status_id':str(user_profile.status_id),
    'photo':user_profile.photo,
    'job_title':user_profile.job_title,
    'department':user_profile.department,
    'company_title':user_profile.company_title,
    'company_info':user_profile.company_info,
    'company_links':user_profile.company_links,
    'links':user_profile.links,
    'contact_info':user_profile.contact_info
}

    if user_profile is None:
        raise PermissionDenied()
    return render(request, 'MyProfile/main_profile.html', ctx)

@login_required
def enter_info(request):
    return render(request, 'MyProfile/my_form.html')

@login_required
def create(request):
        task=request.POST.get("status_id")
        task1=request.POST.get("firstname")
        task2=request.POST.get("lastname")
        task3=request.POST.get("sername")
        task4=request.POST.get("photo")
        task5=request.POST.get("birth_date")
        task6=request.POST.get("email")
        task7=request.POST.get("skills")
        task8=request.POST.get("extrainfo")
        task9=request.POST.get("contact_info") 
        task0=request.POST.get("links")

        user_profile = Profile.objects.create(status_id=task,firstname=task1,lastname=task2,sername=task3,photo=task4,birth_date=task5,email=task6,skills=task7,extrainfo=task8,contact_info=task9,links=task0)

        user_profile.save()
        
        context = {
        'status_id':task,
        }
       
        return render(request, 'MyProfile/extra_form.html', context)


@login_required
def extra_view(request):
    task=request.POST.get("direction",0)
    task1=request.POST.get("graduate_date",0)
    task2=request.POST.get("job_title",0)
    task3=request.POST.get("departament",0)
    #task4=request.POST.get("job_title_com")
    task5=request.POST.get("company_title",0)
    task6=request.POST.get("company_links",0)
    task7=request.POST.get("company_info",0)

    user_profile = Profile.objects.create(direction=task,graduate_date=task1,job_title=task2,department=task3,company_title=task5,company_links=task6,company_info=task7)

    user_profile.save()

    return render(request, 'MyProfile/main_profile.html')
