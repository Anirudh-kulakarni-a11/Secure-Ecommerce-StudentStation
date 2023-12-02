from allauth.account.adapter import DefaultAccountAdapter
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
import pyotp

class TwoFactorAdapter(DefaultAccountAdapter):
    def login(self, request, user):
        if user.is_two_factor_enabled():
            # Generate OTP
            totp = pyotp.TOTP(user.totp_secret)
            otp_code = totp.now()
            
            # Send OTP via email
            send_mail(
                subject="Your Login OTP",
                message=f"Your OTP is: {otp_code}",
                from_email="from@example.com",
                recipient_list=[user.email],
            )
            
            # Save user's ID in the session for later verification
            request.session['2fa_user_id'] = user.id
            
            # Redirect to 2FA verification page
            return redirect(reverse('two_factor_verify'))
        return super().login(request, user)
