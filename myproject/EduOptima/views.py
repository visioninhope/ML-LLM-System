from django.shortcuts import render

# Create your views here.

# views.py

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

    # Create a new user
    user = User.objects.create_user(username=username, password=password, email=email)

    return Response('User registered successfully!')

# views.py

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    password = request.data['password']

    # Authenticate user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Log in the user
        login(request, user)
        return Response('Login successful!')
    else:
        return Response('Invalid credentials!')

# views.py

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def password_reset(request):
    email = request.data['email']

    # Create password reset form
    form = PasswordResetForm({'email': email})
    
    if form.is_valid():
        # Generate password reset token
        token = default_token_generator.make_token(form.user_cache)

        # Send password reset email
        send_mail(
            'Password Reset',
            f'Reset your password by clicking this link: example.com/reset/{token}',
            'admin@example.com',
            [email],
            fail_silently=False,
        )

        return Response('Password reset email sent!')
    else:
        return Response('Invalid email!')

