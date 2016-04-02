from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import formats
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
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
            subject = 'Your Artwork has been approved!'
            message = 'Your recent upload to the Concordia Art System has been approved by our staff!'
            from_email = 'GalleryX@concordia.ca'
            to_email = w.artist.email
            send_mail(subject, message, from_email, [to_email])
        else:
            w.reject()
            subject = 'Your Artwork has been rejected'
            message = 'Your recent upload to the Concordia Art System has been rejected by our staff.'
            from_email = 'GalleryX@concordia.ca'
            to_email = w.artist.email
            send_mail(subject, message, from_email, [to_email])
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
            #Send email to staff
            subject = 'New Artwork Pending'
            message = 'There is a new upload on the Concordia Art Management System waiting for your approval.'
            from_email = 'GalleryX@concordia.ca'
            send_mail(subject, message, from_email, ['rametta@outlook.com'])
            return redirect('work')
    else:
        form = gallery.forms.WorkForm()

    return render(request, 'add_work.html', {'form': form})


@staff_member_required
def staff(request):
    # SELECT * FROM gallery_work WHERE status = 'pending'
    work = Work.objects.filter(status = 'pending')
    return render(request, 'staff.html', {'pending': work})

def faq(request):
    return render(request, 'faq.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        user = request.GET['user']
        work_title = request.GET['title']
        start = datetime.strptime(request.GET['start'], '%Y-%m-%d').date()
        end = datetime.strptime(request.GET['end'], '%Y-%m-%d').date()
        error = False
        if query == 'artist':
            results = User.objects.filter(username__icontains=user, date_joined__range=[start,end])
        else:
            results = Work.objects.filter(title__icontains=work_title, approved_date__range=[start,end], status='approved')
        if not results:
            error = True
        return render(request, 'search.html',{'results': results, 'query': query, 'error': error})
    else:
        return render(request, 'search.html')
