from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the core's index.")

def event(request):
    return HttpResponse("This is event placeholder")