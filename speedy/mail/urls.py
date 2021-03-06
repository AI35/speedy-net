from django.conf.urls import url, include

from speedy.core import admin
from speedy.core.urls_without_login import urlpatterns

app_name = 'speedy.mail'
urlpatterns += [
    url(regex=r'^admin/', view=admin.site.urls),
    url(regex=r'^', view=include('speedy.mail.main.urls', namespace='main')),
]


