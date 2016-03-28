from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gallery.models import Work
from gallery.forms import WorkForm

def index(request):
    return render(request, 'index.html')

def work(request):
    all_work = Work.objects.raw('SELECT * FROM gallery_work')
    return render(request, 'work.html', {'all_work': all_work,})

def artists(request):
    all_artists = User.objects.raw('SELECT * FROM auth_user')
    return render(request, 'artists.html', {'all_artists': all_artists,})

def view_artist(request, username):
    artist = User.objects.raw('SELECT * FROM auth_user where username = %s', [username])[0]
    return render(request, 'view_artist.html', {'artist': artist,})

@login_required
def add_work(request):
    if request.method == 'POST':
        form = WorkForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.artist = request.user
            work.save()
            return redirect('work')
    else:
        form = WorkForm()
        
    return render(request, 'add_work.html', {'form': form})