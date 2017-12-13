"""
Definition of urls for WWEPredictionsProject.
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
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
	url(r'^statistics', app.views.statistics, name='statistics'),
	url(r'^add_wrestler', app.views.add_wrestler, name='add_wrestler'),
    url(r'^edit_wrestler', app.views.edit_wrestler, name='edit_wrestler'),
    url(r'^delete_wrestler', app.views.delete_wrestler, name='delete_wrestler'),
    url(r'^view_wrestler', app.views.view_wrestler, name='view_wrestler'),
	url(r'^select_event', app.views.select_event, name='select_event'),
	url(r'^add_event', app.views.add_event, name='add_event'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]