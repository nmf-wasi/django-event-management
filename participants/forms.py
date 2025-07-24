from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.forms import AuthenticationForm
from event.forms import StyleClassMixin
from django import forms
import re

class SignUpForm(StyleClassMixin,forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'px-2 rounded-lg input-style', 'placeholder': 'Enter password'}),label='Password')
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'px-2 rounded-lg input-style', 'placeholder': 'Enter password'}),label='Confirm Password')

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email','password1', 'confirm_password',]

    # for field errors
    def clean_password1(self):
        password1=self.cleaned_data.get('password1')
        print(password1)
        errors=[]
        if len(password1)<8:
            errors.append("Password must be at least 8 character long!")
        if not re.search(r'[A-Z]', password1):
            errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password1):
            errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password1):
            errors.append("Password must contain at least one number.")
        if not re.search(r'[@#$%^&+=]', password1):
            errors.append("Password must contain at least one special character (@#$%^&+=).")

        if errors:
            raise forms.ValidationError(errors)
        return password1
    
    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password1')
        confirm_password=cleaned_data.get('confirm_password')

        if password1!=confirm_password:
            raise forms.ValidationError("Passwords don't match")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles()   


class LoginForm(StyleClassMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles() 


class assignRoleForm(StyleClassMixin,forms.Form):
    role=forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a Role",
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles() 


class CreateGroupForm(StyleClassMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )
    
    class Meta:
        model = Group
        fields = ['name', 'permissions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles() 