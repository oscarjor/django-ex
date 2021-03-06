from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from happ.views import employee, employer

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^employee$', employee),
    url(r'^employer$', employer),
    url(r'^admin/', include(admin.site.urls)),
]
