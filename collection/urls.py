from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from gallery import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)


urlpatterns = [
    # Artist / Work URL's
    url(r'^$', views.index, name ='home'),
    url(r'^work/$', views.work, name='work'),
    url(r'^work/add/$', views.add_work, name='add_work'),
    url(r'^work/(?P<id>[0-9]+)/$', views.view_work, name='view_work'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^artist/(?P<id>[0-9]+)/$', views.view_artist, name='view_artist'),
    url(r'^staff/$', views.staff, name='staff'),
    # Account URL's
    url(r'^accounts/password/reset/$',password_reset,{'template_name': 'registration/password_reset_form.html'},name="password_reset"),
    url(r'^accounts/password/reset/done/$',password_reset_done,{'template_name': 'registration/password_reset_done.html'},name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9AZa-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm,{'template_name': 'registration/password_reset_confirm.html'},name="password_reset_confirm"),
    url(r'^accounts/password/done/$',password_reset_complete,{'template_name': 'registration/password_reset_complete.html'},name="password_reset_complete"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # Admin URL's
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    
    
    