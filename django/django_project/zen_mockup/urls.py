from django.conf.urls import include, url
from zen_mockup import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.zen_mockup, name='zen_mockup')
]
