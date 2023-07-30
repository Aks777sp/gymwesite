# forms.py in your members app

from django import forms
from .models import Member, Post


class MemberRegistrationForm(forms.ModelForm):
    subscription_ends = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'password', 'subscription_ends', 'social_id', 'is_staff', 'telephone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'social_id': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'telephone', 'social_id']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']