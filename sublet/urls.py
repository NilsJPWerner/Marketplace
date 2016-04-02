from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'^', include('listings.urls', namespace="listings")),

    # Main pages
    url(r'^$', TemplateView.as_view(template_name="sublet/landing.html"), name="landing"),
    url(r'^search/$', views.search, name="search"),
    url(r'^user/(?P<user>[0-9A-Za-z]+)/$', views.public_profile, name="public_profile"),
    url(r'^contact/$', views.contact, name="contact"),

    # ajax
    url(r'^star/$', views.ajax_star, name="star"),


    # Profile tools
    url(r'^accounts/', include('allauth.urls'), name='accounts'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
