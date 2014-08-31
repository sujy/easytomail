#!/usr/bin/env python
from django.core.mail import send_mail
from django.http import *
from django.shortcuts import render_to_response
# Create your views here.
def mail(request):
    errors = []
    if request.method == 'GET':
        return render_to_response('mail.html',{'errors': errors})    
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Please enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Pleas enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'], 
                request.POST['message'], 
                'easytomailadmin@163.com',
                [request.POST['email']],
            )
            return HttpResponseRedirect('/thanks/')
    return render_to_response('mail.html',{'errors': errors})