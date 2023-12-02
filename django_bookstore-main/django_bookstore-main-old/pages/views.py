from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from books.models import Book, Order
import stripe
from decimal import Decimal

# Initialize Stripe with the secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)

        book_id = session.book_id  # Replace with actual book ID retrieval logic
        amount = Decimal(session.amount_total) / 100  # Stripe amounts are in cents

        # Fetch the book instance
        book = Book.objects.get(id=book_id)

        # Create and save the order
        order = Order(user=request.user, book=book, amount=amount)
        order.save()

    return redirect('home')

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)

        # Convert amount to decimal
        amount = Decimal(session.amount_total) / 100  # Stripe amounts are in cents

        # Logic to create and store the order
        order = Order(user=request.user, book_id='book_id', amount=amount)
        order.save()

    return redirect('home')

def payment_cancel(request):
    return render(request, 'cancel.html')

def stripe_checkout(request):
    if request.method == 'POST':
        # Create Stripe Checkout Session
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 1000,  # Set the amount
                        'product_data': {
                            'name': 'Your Book Name',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),  # Your success URL
                cancel_url=request.build_absolute_uri('/cancel/'),  # Your cancel URL
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})  # Error page
    else:
        # Render or redirect to the page with Stripe Checkout button
        return render(request, 'checkout.html')  # Your checkout page template

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_5_books = Book.objects.all().order_by("-date_creation")[:5][::-1]
        context["last_5_books"] = last_5_books
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
