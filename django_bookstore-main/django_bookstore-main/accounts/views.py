from django.contrib.auth import login as auth_login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserUpdateProfileForm
from django.core.mail import send_mail
from .models import CustomUser

def send_otp_email(user):
    otp = ''.join(str(ord(c)) for c in user.email[:5])
    send_mail(
        'Your OTP',
        f'Your OTP is: {otp}',
        'vckkrocks@gmail.com', 
        [user.email],
        fail_silently=True,
    )

def is_valid_2fa_code(user, code):
    return user.verify_totp(code)

def verify_two_factor_code(request):
    if request.method == 'POST':
        user_id = request.session.get('otp_user_id')
        if not user_id:
            return redirect('account_login')  # Redirect to login page if session is missing

        user = get_user_model().objects.get(id=user_id)
        otp_provided = request.POST.get('code')
        expected_otp = ''.join(str(ord(c)) for c in user.email[:5])

        if otp_provided == expected_otp:
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            del request.session['otp_process']
            del request.session['otp_user_id']  # Clear the session variables
            return redirect('home')  # Redirect after successful login
        else:
            messages.error(request, 'Incorrect OTP. Please try again.')

    return render(request, 'two_factor_verify.html')  # Path to your OTP verification template

class UpdateProfileView(LoginRequiredMixin, FormView):
    template_name = "account/update_profile.html"
    form_class = CustomUserUpdateProfileForm
    success_url = reverse_lazy("account_profile")

    def dispatch(self, request, *args, **kwargs):
        """Will send a notification in case user is not logged"""
        if not request.user.is_authenticated:
            messages.error(self.request, "You need to log in to check your profile")
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super(UpdateProfileView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({"username": self.request.user})
        return initial

    def form_valid(self, form):
        new_username = form.cleaned_data.get("username", None)
        if new_username is not None:
            actual_user = get_user_model().objects.get(username=self.request.user)
            actual_user.username = new_username
            actual_user.save()
            messages.success(self.request, "Profile Updated!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Action denied!")
        return super().form_invalid(form)
