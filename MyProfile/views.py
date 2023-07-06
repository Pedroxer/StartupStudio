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
        return redirect('MyProfile/change')
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
   
def create_profile(request):
    return render(request, 'MyProfile/my_form.html')

def create(request):
    
    return render(request, 'MyProfile/main_profile.html')



# Create your views here.
