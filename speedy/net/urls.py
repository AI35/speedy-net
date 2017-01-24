from django.conf.urls import url, include
from django.contrib import admin

from speedy.core.urls import urlpatterns

urlpatterns += [
    url(r'^', include('speedy.net.accounts.urls', namespace='accounts')),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # always at the bottom
    url(r'^(?P<slug>[-\._\w]+)/friends/', include('speedy.core.friends.urls', namespace='friends')),
    url(r'^messages/', include('speedy.core.im.urls_private', namespace='im')),
    url(r'^messages/(?P<slug>[-\._\w]+)/', include('speedy.core.im.urls_public', namespace='im_entity')),
    url(r'^(?P<slug>[-\._\w]+)/blocks/', include('speedy.core.blocks.urls', namespace='blocks')),
    url(r'^uploads/', include('speedy.core.uploads.urls', namespace='uploads')),
    url(r'^', include('speedy.core.profiles.urls', namespace='profiles')),
]
