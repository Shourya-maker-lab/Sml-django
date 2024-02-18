from django.shortcuts import render 
from .models import CarouselImage



# Create your views here.
def index(request):
    carousel_images = CarouselImage.objects.all()
    return render(request, 'index.html', {'carousel_images': carousel_images})

