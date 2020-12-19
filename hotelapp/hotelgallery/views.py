from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HotelForm
# Create your views here.


def Hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'gallery/image.html', {'form': form})


def success(request):
    return HttpResponse("successfully uploaded")
