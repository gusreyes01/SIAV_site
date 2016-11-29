from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from website.forms import FormaContacto, FormaSuscripcion

def send_mail_wrapper(title, template, context, recipients):
    html_message = render_to_string(
        template, context)
    send_mail(title,
              html_message,
              '',
              recipients,
              html_message=html_message,
              fail_silently=False)


def index(request):
  page = 'home_page'
  suscripcion = FormaSuscripcion()
  forma = FormaContacto()
  return render(request, 'index.html', locals())


@csrf_exempt
def contact(request):
    if request.method == 'POST':
    	nombre = request.POST['nombre']
    	email = request.POST['email']
    	mensaje = request.POST['mensaje']

    	context = {
    		'nombre': nombre,
    		'email': email,
    		'mensaje': mensaje,
    	}
       
        send_mail_wrapper('Mensaje de tu portal ',
                          'email_template.html',
                          context, ['dul.rdzs@gmail.com'])

        return HttpResponse('')


@csrf_exempt
def suscripcion(request):
  if request.method == 'POST':
    email_suscripcion = request.POST['email_suscripcion']

    context = {'email_suscripcion': email_suscripcion,}

    send_mail_wrapper('Mensaje de tu portal ',
                      'email_template.html',
                      context, ['dul.rdzs@gmail.com'])

    return HttpResponse('')


def planes(request):
  page = 'pricing_page'
  return render(request, 'pricing.html', locals())


def producto(request):
  page = 'features_page'
  return render(request, 'producto.html', locals())

def producto_option(request, option):
  page = 'features_page'
  select_tab = option
  return render(request, 'producto.html', locals())


def contacto(request):
  page = 'contact_page'
  return render(request, 'contacto.html', locals())


def faq(request):
  page = 'faq_page'
  return render(request, 'faq.html', locals())
