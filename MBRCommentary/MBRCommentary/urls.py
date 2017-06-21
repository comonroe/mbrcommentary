"""
Definition of urls for MBRCommentary.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^editcogs/(?P<OrgDetail>\w+)/$', app.views.edit_cogs, name='edit_cogs'),
    url(r'^editopex/(?P<OrgDetail>\w+)/$', app.views.edit_opex, name='edit_opex'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
