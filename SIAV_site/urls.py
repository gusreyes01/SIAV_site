from django.conf.urls import url
from django.contrib import admin

import website.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', website.views.index, name='index'), 
    url(r'^contact/', website.views.contact, name='contact'),
    url(r'^suscripcion/', website.views.suscripcion, name='suscripcion'),
    url(r'^planes/', website.views.planes, name='planes'),
    url(r'^producto/', website.views.producto, name='producto'),
    url(r'^contacto/', website.views.contacto, name='contacto'),
    url(r'^faq/', website.views.faq, name='faq'),
]