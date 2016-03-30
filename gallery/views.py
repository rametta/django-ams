from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from gallery.models import Work
import gallery.forms


def index(request):
    # SELECT * FROM gallery_work WHERE status = 'approved' ORDER BY submit_date DESC
    approved_work = Work.objects.filter(status='approved').order_by('-submit_date')
    return render(request, 'index.html', {'approved': approved_work})


def work(request):
    # SELECT * FROM gallery_work WHERE status = 'approved'
    approved_work = Work.objects.filter(status='approved')
    return render(request, 'work.html', {'approved': approved_work})


def view_work(request, id):
    if request.method == 'POST':
        choice = request.POST.get('approve')
        w = Work.objects.get(id=id)
        if choice == 'approve':
            w.approve()
        else:
            w.reject()
        return redirect('view_work', id=id)
    elif request.method == 'GET':
        # SELECT * FROM gallery_work WHERE id = id
        work = Work.objects.get(id=id)
        return render(request, 'view_work.html', {'work': work})


def artists(request):
    # SELECT * FROM auth_user ORDER BY id ASC
    all_artists = User.objects.all().order_by('id')
    return render(request, 'artists.html', {'all_artists': all_artists})


def view_artist(request, id):
    # SELECT * FROM auth_user WHERE username = username
    artist = User.objects.get(id=id)
    # SELECT * FROM gallery_work WHERE artist = id
    work = Work.objects.filter(artist=id, status='approved')
    # SELECT COUNT(*) FROM gallery_work WHERE id = id
    # SELECT COUNT(*) FROM gallery_work WHERE id = id AND status = 'pending'
    # SELECT COUNT(*) FROM gallery_work WHERE id = id AND status = 'approved'
    # SELECT COUNT(*) FROM gallery_work WHERE id = id AND status = 'rejected'
    count = {'submission': Work.objects.filter(artist=id).count(),
             'pending': Work.objects.filter(artist=id, status='pending').count(),
             'approved': Work.objects.filter(artist=id, status='approved').count(),
             'rejected': Work.objects.filter(artist=id, status='rejected').count()
             }
    return render(request, 'view_artist.html', {'artist': artist, 'work': work, 'count': count})


@login_required
def add_work(request):
    if request.method == 'POST':
        form = gallery.forms.WorkForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.artist = request.user
            work.save()
            return redirect('work')
    else:
        form = gallery.forms.WorkForm()

    return render(request, 'add_work.html', {'form': form})


@staff_member_required
def staff(request):
    # SELECT * FROM gallery_work WHERE status = 'pending'
    work = Work.objects.filter(status = 'pending')
    return render(request, 'staff.html', {'pending': work})
