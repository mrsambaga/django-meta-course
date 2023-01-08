from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from myapp.models import Menu

# Create your views here.
def home(request):
    return render(request, 'home.html')

#def book(request):
#   return render(request, 'book.html')


def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment'
    }

    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "book.html", context)

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all()
    item_dict = {'menu':menu_items}
    return render(request, "menu.html", item_dict)

def display_menu_items(request, pk=None) :
    if pk :
        menu_item = Menu.objects.get(pk=pk)
    else :
        menu_item = ''
    render(request, 'menu_item.html', {"menu_item" : menu_item})

