from django.forms import ModelForm, PasswordInput, EmailInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import CustomUser, models
from django.contrib.auth import get_user_model


User = get_user_model()



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


    #f_name = forms.Charfield(max_length=100)
    #l_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.CharField(widget=EmailInput)
    #psw = forms.CharField(widget=PasswordInput)
    #psw_c = forms.CharField(widget=PasswordInput)