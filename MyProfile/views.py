from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from MyProfile.models import Profile
from UserSystem.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from core.models import Project

@login_required
def main_profile(request):
    try:
        user_profile = Profile.objects.get(email=request.user.email)
    except Profile.DoesNotExist:
        return redirect('MyProfile/ent')

    projects = Project.objects.filter(Q(project_authors=request.user.id)|Q(project_participants=request.user.id))

    ctx = {'firstname':user_profile.firstname,
    'lastname':user_profile.lastname,
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
    'contact_info':user_profile.contact_info,
    'project_list':projects
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
        'email':task6,
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

    task0=request.POST.get('secret')


    user_profile = Profile.objects.filter(email=task0).update(direction=task,graduate_date=task1,job_title=task2,department=task3,company_title=task5,company_links=task6,company_info=task7)

    #user_profile.save()

    return render(request, 'MyProfile/main_profile.html')

@login_required
def change(request):
    user_profile = Profile.objects.get(email=request.user.email)
    ctx = {'first_name':user_profile.firstname,
    'last_name':user_profile.lastname,
    'sername':user_profile.sername,
    'birth_date': user_profile.birth_date,
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
    return render(request, 'MyProfile/create_form.html',ctx)

@login_required
def delete_profile(request):
     user_profile = Profile.objects.get(email=request.user.email)
     user_profile.delete()
     return redirect('/news')

@login_required
def update(request):
        #user_profile = Profile.objects.get(email=request.user.email)
        task0=request.POST.get('secret')

        #task=request.POST.get("status_id")
        task1=request.POST.get("firstname")
        task2=request.POST.get("lastname")
        task3=request.POST.get("sername")
        task4=request.POST.get("photo")
        #task5=request.POST.get("birth_date")
        # task6=request.POST.get("email")
        task7=request.POST.get("skills")
        task8=request.POST.get("extrainfo")
        task9=request.POST.get("contact_info") 
        task10=request.POST.get("links")
        task11=request.POST.get("direction",0)
        #task1=request.POST.get("graduate_date",0)
        task12=request.POST.get("job_title",0)
        task13=request.POST.get("department",0)
        #task4=request.POST.get("job_title_com")
        task15=request.POST.get("company_title",0)
        task16=request.POST.get("company_links",0)
        task17=request.POST.get("company_info",0)

      
       
        user_profile = Profile.objects.filter(email=task0).update(firstname=task1,lastname=task2,sername=task3,photo=task4,skills=task7,extrainfo=task8,contact_info=task9,links=task10,direction=task11,job_title=task12,department=task13,company_title=15,company_links=task16,company_info=task17)

        # user_profile.save()
       
        return render(request, 'MyProfile/main_profile.html')