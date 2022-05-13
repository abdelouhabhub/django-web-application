from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from app.models import CustomUser
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from app.forms import RegisterForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model


User = get_user_model()

def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('TEACHER Dashboard!!')
            elif user_type == '3':
                return HttpResponse('STUDENT Dashboard!!')
            else:
                messages.error(request, 'Email and Password are invalid!')
                return redirect('login')
        else:
            messages.error(request, 'Invalid Email or Password!')
            return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        'user':user,
    }
    return render(request, 'profile.html', context)


def doLOGOUT(request):
    return redirect(request, 'login')


def FORMS(request):
    return redirect(request, 'forms')

@login_required(login_url='/')
def EDITED_PROFILE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.FILES.get('email')
        #username = request.FILES.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic

            if password != None and password != '':
                customuser.set_password(password)
            if profile_pic != None and profile_pic != '':
                customuser.set_profile_pic(profile_pic)
            customuser.save()
            messages.success(request, 'Profile Updated Successufully!')
            redirect('profile')
        except:
            messages.error(request, 'Error! Failed to Update!')

    return render(request, 'profile.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.save()
            #login(request, user)
            #messages.success(request, "Register Successuful")
        return redirect('home')
        #messages.error(request, "Unsuccessful Registration. Invalid Information")
    else:
        form = RegisterForm()
    return render(request, "register.html", context={"form":form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = 'password/password_reset_email.txt'
                    c = {
                        "email":user.email,
                        "domain":'127.0.0.1.8000',
                        'site_name':'Website',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocool': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('/password_reset/done/')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='password/password_reset.html',context={'password_reset_form':password_reset_form})


def home(request):
    return render(request, 'home.html')