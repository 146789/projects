from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar

# Create your views here.


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = f"MyClub Event Calander - {month_name} {year}"
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, 'Dem/Base.html', {'title': title, 'cal': cal})

