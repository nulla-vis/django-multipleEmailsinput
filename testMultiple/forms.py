from django import forms
from django.forms import fields
from .models import User, Email


class EmailListsForm(forms.Form):
    emailList = forms.CharField(widget=forms.HiddenInput())


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email_list',)


class EmailsForm(forms.Form):
    email = forms.EmailField(required=True)
