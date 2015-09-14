from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^javapic_javascript/', include('javapic_javascript.urls')),
    url(r'^javapic_javascript/', include('javapic_javascript.urls')),

    url(r'^javapic_jquery/', include('javapic_jquery.urls')),
    url(r'^table_of_contents/', include('table_of_contents.urls')),
    url(r'^zen_mockup/', include('zen_mockup.urls'))
]
