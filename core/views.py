from django.forms import DateInput
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Project
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .forms import NewUserForm, CreateProjectForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return HttpResponse("Hello, world. You're at the core's index.")


def event(request):
    latest_projects_list = Project.objects.all()
    return HttpResponse(
        "This is event placeholder:" + latest_projects_list[0].project_name + " " + latest_projects_list[
            0].project_info)


#should implement checking user permissions here (can manage the project? is the project owner? can join the project?)
class ProjectDetailedView(generic.DetailView): #also check if already joined the project and check status of joining
    model = Project
    template_name = 'core/project_detail.html'


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'core/project_list.html'

    def get_queryset(self):
        queryset = Project.objects.filter(project_status__in=['acc', 'act', 'fin'])
        return queryset #using multiple values to filter out only those posts that aren't denied


#depricated
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


#depricated
def login_view(request): ##Это все надо переделать через встроенные view
    if request.method == "POST":
        user = authenticate(username='Will', password='hah')
        if user is not None:
            login(request, user)
    form = NewUserForm()
    return render(request=request, template_name="core/login.html", context={"register_form": form})

#books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
#^ filter using name of a Foreign key field's name
#type__cover__name__exact - filtering using multiple levels of Foreign keys
# book -> FK type -> FK cover -> cover name


class ProjectCreate(CreateView):
    model = Project
    form_class = CreateProjectForm
#swap with a custom form actually, so I can actually save user info as well


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['project_name', 'project_info', 'event_type', 'direction_type', 'project_skills', 'project_start',
              'project_end', ]
    labels = {'project_name': 'Название проекта', 'project_info': 'Информация о проекте',
              'event_type': 'Название направления', 'project_skills': 'Навыки мероприятия',
              'project_start': 'Начало проекта', 'project_end': 'Конец проекта'}


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('event_list')


#using custom form and view in order to implement user saving
@permission_required('core.can_create_projects')
def create_project_view(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = models.Project(project_name=form.project_name, project_info=form.project_info, event_type=form.event_type, direction_type=form.direction_type, project_start=form.project_start, project_end=form.project_end)
            project.project_authors.add(request.user)
            project.save()
            return HttpResponseRedirect(reverse('core:project_detail', args=[int(project.id)]))
    else:
        form = CreateProjectForm()
        return render(request, 'core/project_form.html', {'form': form})


@permission_required('core.can_moderate_projects')
def accept_new_projects_view(request):
    pending_projects = Project.objects.filter(project_status='pen')
    return render(request, 'core/new_projects_mod.html', {'object_list': pending_projects})


@permission_required('core.can_moderate_projects')
def accept_project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.project_status = 'acc'
    project.save()
    return redirect('core:new_projects_mod')


@permission_required('core.can_moderate_projects')
def deny_project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.project_status = 'den'
    project.save()
    return redirect('core:new_projects_mod')


#three views below are not tested
def start_project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.project_authors.contains(request.user) or request.user.is_superuser:
        project.project_status = 'act'
        project.save()
    return redirect('core:project_detail', args=[pk])


def finish_project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.project_authors.contains(request.user) or request.user.is_superuser:
        project.project_status = 'fin'
        project.save()
    return reverse('core:project_detail', args=[pk])


def enter_the_project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if not project.project_authors.contains(request.user) and not models.ProjectEntry.objects.filter(user=request.user, project=project):
        project_entry = models.ProjectEntry(user=request.user, project=project)
        project_entry.save()
    return reverse('core:project_detail', args=[pk])



