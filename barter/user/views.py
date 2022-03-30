from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string

from .forms import *
from .models import *


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.POST:

        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():

            user = signup_form.save(commit=False)
            user.set_password(signup_form.cleaned_data['password'])
            user.save()

            Verification.objects.get(email=user.email).delete()

            login(request, user)

            return redirect('home')

    return render(request, "signup.html")


def login_handler(request):

    username, error = '', False

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True

    return render(request, 'login.html', context={'error': error, 'username': username})


@login_required
def logout_handler(request):
    logout(request)
    return redirect('login')


def check_username(request):

    try:
        User.objects.get(username=request.GET.get('username'))
    except:
        return JsonResponse({'exists': False})

    return JsonResponse({'exists': True})


def check_email(request):

    try:
        User.objects.get(email=request.GET.get('email'))
    except:
        return JsonResponse({'exists': False})

    return JsonResponse({'exists': True})


def check_code(request):

    email = request.GET.get("email")
    code = request.GET.get("code")

    try:
        is_correct = (code == Verification.objects.get(email=email).code)
    except:
        is_correct = False

    return JsonResponse({'is_correct': is_correct})


def send_code(request):

    # Sends 4 digit code to the email found in the request
    def generate_code():
        """ Generates random four digits code"""

        import random
        import math

        return "".join([str(math.floor(random.random() * 10)) for _ in range(4)])

    name = request.GET.get("name")
    email = request.GET.get("email")
    code = generate_code()

    Verification(email=email, code=code).save()

    subject = "Barter Verification Code"
    message = f"Dear {name}, use {code} to signup."
    html_message = render_to_string('verification_message.html', context={
                                    'name': name, 'code': code})

    send_mail(subject,
              message,
              "barterethiopia@gmail.com",
              [email],
              html_message=html_message,
              )


@login_required
def delete_profile(request):

    request.user.delete()

    return redirect('login')
