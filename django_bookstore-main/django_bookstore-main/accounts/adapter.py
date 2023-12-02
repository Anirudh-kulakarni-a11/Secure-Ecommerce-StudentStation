# accounts/adapter.py

from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail
import pyotp

class CustomAccountAdapter(DefaultAccountAdapter):
    def login(self, request, user):
        # Generate OTP and send email
        otp = ''.join(str(ord(c)) for c in user.email[:5])
        send_mail(
            'Your OTP',
            f'Your OTP is: {otp}',
            'vckkrocks@gmail.com',
            [user.email],
            fail_silently=False,
        )
        
        # Store user's ID in the session but don't log them in yet
        request.session['otp_user_id'] = user.id
        request.session['otp_process'] = True
        # Redirect to OTP verification page
        return redirect(reverse('two_factor_verify'))
   
    def get_login_redirect_url(self, request):
        if 'otp_process' in request.session:
            # Redirect to OTP verification page
            return reverse('two_factor_verify')
        else:
            # Use the default redirect logic
            return super().get_login_redirect_url(request)