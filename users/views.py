from django.http import HttpResponse

def blank_response(request):
    return HttpResponse("nothing to see")
