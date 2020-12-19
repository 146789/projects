from django.shortcuts import render
from django.http import HttpResponse
from cookiesapp.forms import ItemForm
# Create your views here.


def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Home page</h1>")


def page2(request):
    if request.session.test_cookie_worked():
        print("cookies are enabled")
    request.session.delete_test_cookie()
    return HttpResponse("page2")


def countview(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count = 1
    response = render(request, 'cookieapp/count.html', {'count': count})
    response.set_cookie('count', count)
    return response


def index(request):
    return render(request, 'cookieapp/index.html')


def addItem(request):
    form = ItemForm()
    response = render(request, 'cookieapp/additem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 120)

    return response


def displayKart(request):
    return render(request, 'cookieapp/displayItem.html')
