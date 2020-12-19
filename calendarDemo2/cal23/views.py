from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event

# Create your views here.


def base1(request):
    return render(request, 'base.html')


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date': '09-20-2020',
            'announcement': 'Sunrisers hyderabad'
        },
        {
            'date': '09-30-2020',
            'announcement': 'Royal Challengers Banglore'
        }
    ]
    return render(request, 'cal23/calbase.html', {'title': title, 'cal': cal, 'announcements': announcements})


def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'cal23/event_list.html', {'events_list': events_list})
