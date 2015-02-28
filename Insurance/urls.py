from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from InsuranceItem import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Insurance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^(?P<applyNum>\d*)/$',views.detail),
    url(r'^newone/$',views.newone),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/$', views.update),
    url(r'^add/$', views.add),
    url(r'^search/$', views.search),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
