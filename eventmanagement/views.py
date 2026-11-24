
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .models import EventEnquiry


# Home Page
def homepage(request):
    return render(request, 'homepage.html')


# Events Page
def events(request):
    return render(request, 'Event.html')


# About Page
def aboutus(request):
    return render(request, 'Aboutus.html')


# Contact Page
def contact(request):
    return render(request, 'Contactus.html')


# Services Page
def service(request):
    return render(request, 'services.html')


# Signup
def signup(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        # Check password confirmation
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check whether email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        # Check whether username already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Account already exists.")
            return render(request, 'signup.html')

        # Create user using Django authentication
        User.objects.create_user(
            username=email,
            first_name=name,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Registration successful! Please login."
        )

        return redirect('login')

    return render(request, 'signup.html')


# Login
def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)

            return redirect('homepage')

        else:
            messages.error(
                request,
                "Invalid email or password."
            )

    return render(request, 'login.html')


# Logout
def logout(request):

    auth_logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect('homepage')

@login_required(login_url='login')
def planyourevent(request):

    if request.method == "POST":

        EventEnquiry.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            contact_method=request.POST.get('contact_method'),
            event_type=request.POST.get('event_type'),
            event_date=request.POST.get('event_date'),
            event_location=request.POST.get('event_location'),
            guest_count=request.POST.get('guest_count'),
            budget=request.POST.get('budget'),
            event_duration=request.POST.get('event_duration'),
            services=request.POST.getlist('services'),
            requirements=request.POST.get('requirements'),
        )

        messages.success(
            request,
            "Thank you for choosing EverAfter! "
            "Your event enquiry has been submitted successfully. "
            "Our team will contact you soon to discuss your "
            "requirements and provide further assistance."
        )

        return redirect('planyourevent')

    return render(request, 'planyourevent.html')

