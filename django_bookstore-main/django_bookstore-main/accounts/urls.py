from django.urls import path
from .views import verify_two_factor_code
from .views import UpdateProfileView

urlpatterns = [
    path("profile/", UpdateProfileView.as_view(), name="account_profile"),
    path('verify-2fa/', verify_two_factor_code, name='two_factor_verify'),
]
