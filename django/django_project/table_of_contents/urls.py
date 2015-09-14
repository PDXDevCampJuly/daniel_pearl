from django.conf.urls import include, url
from table_of_contents import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.table_of_contents, name='table_of_contents')
]
