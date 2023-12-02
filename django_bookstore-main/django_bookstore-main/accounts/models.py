from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    totp_secret = models.CharField(max_length=100, default='dummy-secret')  # Not used in hard-coded version
    is_2fa_enabled = models.BooleanField(default=True)  # Field to track if 2FA is enabled

    def generate_otp_from_email(self):
        # Simplified OTP generation based on email
        return ''.join(str(ord(c)) for c in self.email[:5])

    def verify_totp(self, token):
        # Check if the provided token matches the generated OTP
        expected_otp = self.generate_otp_from_email()
        return token == expected_otp

    def is_two_factor_enabled(self):
        return self.is_2fa_enabled