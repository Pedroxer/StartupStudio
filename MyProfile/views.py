

from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


        #print(request.POST['status_id'])
        task=request.POST.get("status_id")

        task1=request.POST.get("firstname")
        # user_profile = Profile.objects.create(firstname=task)
        task2=request.POST.get("lastname")
        # user_profile = Profile.objects.create(lastname=task)
        task3=request.POST.get("sername")
        # user_profile = Profile.objects.create(sername=task)

        task4=request.POST.get("photo")
        # user_profile = Profile.objects.create(photo=task)
        task5=request.POST.get("birth_date")
        # user_profile = Profile.objects.create(birth_date=task)
        task6=request.POST.get("email")
        # user_profile = Profile.objects.create(email=task)
        task7=request.POST.get("skills")
        # user_profile = Profile.objects.create(skills=task)
        task8=request.POST.get("extrainfo")
        # user_profile = Profile.objects.create(extrainfo=task)
        task9=request.POST.get("contact_info")
        # user_profile = Profile.objects.create(contact_info=task)
        task0=request.POST.get("links")
        # user_profile = Profile.objects.create(links=task)

        user_profile = Profile.objects.create(status_id=task,firstname=task1,lastname=task2,sername=task3,photo=task4,birth_date=task5,email=task6,skills=task7,extrainfo=task8,contact_info=task9,links=task0)

        user_profile.save()
        context = {
        'status_id':task,
        }

        # return redirect('')
        return render(request, 'MyProfile/extra_form', context)

@login_required
def extra_view(request):

    return render(request, 'MyProfile/extra_form')


# Create your views here.
