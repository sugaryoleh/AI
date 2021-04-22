from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from diseases.models import Speciality

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    speciality = forms.ChoiceField()
    speciality = forms.MultipleChoiceField(choices=zip((i for i in range(len(Speciality.objects.all()))),
                                                       (s.name for s in Speciality.objects.all())))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'speciality', 'password1', 'password2', )

