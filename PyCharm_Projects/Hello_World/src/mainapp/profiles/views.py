from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def admin_console(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': 'profiles'})