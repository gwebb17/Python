from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    compNames = {"Frederic Chopin", "Ludwig Van Beethoven", "Wolfgang Amadeus Mozart", "Franz Liszt"}
    context = {
        'compNames': compNames,
    }
    return render(request, "home.html", context)