import threading

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect

from django.conf import settings

from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from django.contrib.sites.shortcuts import get_current_site

def create_mail(mail, subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            mail
        ],
        cc=[]
    )
    
    message.attach_alternative(content, 'text/html')
    return message

def index(request):
    return render(request, 'index.html', {})

def send_welcome_mail(request):
    context = {
        'username': 'eduardo_gpg',
        'url': reverse('index'),
        'domain': get_current_site(request).domain,
    }

    email = create_mail(
        'eduardo@codigofacilito.com',
        'Welcome Mail Live!',
        'email/welcome.html',
        context
    )

    email.send(fail_silently=False)

def send_mail(request):
    thread = threading.Thread(target=send_welcome_mail, args=(request,))
    thread.start()

    return redirect('index')