from django.http import HttpResponse
def index (request):
    all_albums = Album.objects.all()
    return HttpResponse("<h1> hello all this is the welcome page of this app </h1>")