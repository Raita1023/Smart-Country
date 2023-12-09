from django.forms import forms
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime
import re
from .models import Appointment


from .models import *


from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

UserB = get_user_model()

class StudentLoginForm(AuthenticationForm):
    Student_id = forms.CharField(max_length=10, required=True)
    Password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username has already been taken.')
        return username


def increase_hour(time):
    new_time = time + datetime.timedelta(hours=1)
    if new_time.minute < time.minute:
        new_time += datetime.timedelta(minutes=60)
    return new_time


def get_number_from_string(string):
  """Extracts the only number value from a string.

  Args:
    string: A string.

  Returns:
    A string containing the only number value in the string, or an empty string
    if no number value is found.
  """

  pattern = r'\d+'
  match = re.search(pattern, string)
  if match:
    return match.group()
  else:
    return ''



def get_text_from_string(string):
  """Extracts the text from a string, excluding any numbers.

  Args:
    string: A string.

  Returns:
    A string containing the text from the string, excluding any numbers, or an
    empty string if no text is found.
  """

  pattern = r'[^\d]+'
  match = re.search(pattern, string)
  if match:
    return match.group()
  else:
    return ''



def extract_district_from_mp(mp_string):
  """Extracts the district name from inside the brackets of a given MP string.

  Args:
    mp_string: A string representing the MP's name and district.

  Returns:
    A string representing the district name, or None if the MP's district cannot be extracted.
  """

  district_pattern = re.compile(r'\(([^)]+)\)', re.IGNORECASE)
  match = district_pattern.search(mp_string)
  if match:
    return match.group(1)
  else:
    return None
  
class AppointmentForm(forms.ModelForm):
      class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'facility', 'date']
class CarForm(forms.ModelForm):
      class Meta:
        model = CarBook
        fields = ['name', 'email', 'phone', 'facility', 'date']
class PlaneForm(forms.ModelForm):
      class Meta:
        model = PlaneBook
        fields = ['name', 'email', 'phone', 'facility', 'date']
class TrainForm(forms.ModelForm):
      class Meta:
        model = TrainBook
        fields = ['name', 'email', 'phone', 'facility', 'date']
    


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)