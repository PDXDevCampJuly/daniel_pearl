from django.conf.urls import include, url
from table_of_contents.views import table_of_contents

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^javapic/', include('javapic.urls')),
    url(r'^javapic_jquery/', include('javapic_jquery.urls')),
    url(r'^zen_mockup/', include('zen_mockup.urls')),
    url(r'^$', table_of_contents, name='table_of_contents.urls')
]
