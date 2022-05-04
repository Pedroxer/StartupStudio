from django.http import HttpResponse

from core.models import Project


def index(request):
    return HttpResponse("Hello, world. You're at the core's index.")

def event(request):
    latest_projects_list = Project.objects.all()
    return HttpResponse("This is event placeholder:" + latest_projects_list[0].project_name + " " + latest_projects_list[0].project_info)