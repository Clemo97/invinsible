from django.shortcuts import render,HttpResponse
from .models import Picture,Location,Category

# Create your views here.
def welcome(request):
    pictures = Picture.objects.all()
    kenya=Picture.filter_by_location(location='Kenya')
    india=Picture.filter_by_location(location='India')
    morocco=Picture.filter_by_location(location='Morocco')
    canada=Picture.filter_by_location(location='Canada')
    return render(request,'all-pictures/index.html',{'pictures':pictures, 'kenya':kenya,'india':india,'morocco':morocco,'canada':canada})

def search_results(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})
