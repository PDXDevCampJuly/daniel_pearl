from django.conf.urls import include, url
from django.contrib import admin
import polls

urlpatterns = [
    # Examples:
    # url(r'^$', 'poll_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^poll/', include('polls.urls', namespace="polls")),

]
