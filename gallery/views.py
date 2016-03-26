from django.shortcuts import render
from django.contrib.auth.models import User
from gallery.models import Work, Upload

def index(request):
    return render(request, 'index.html')

def work(request):
    all_work = Work.objects.all()
    return render(request, 'work.html', {'all_work': all_work,})

def artists(request):
    all_artists = User.objects.all()
    return render(request, 'artists.html', {'all_artists': all_artists,})

def view_artist(request, username):
    artist = User.objects.get(username = username)
    return render(request, 'view_artist.html', {'artist': artist,})

def add_work(request):
    return render(request, 'add_work.html')

