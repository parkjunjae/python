from django.http.response import HttpResponse

def home_views(request):
    return HttpResponse("home test")