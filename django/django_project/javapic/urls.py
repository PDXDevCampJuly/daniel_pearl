from django.conf.urls import include, url
from javapic import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^join', views.join, name='join')
]
