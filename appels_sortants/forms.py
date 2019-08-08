from django import forms
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from datetimepicker.widgets import DateTimePicker




class ContactForm(forms.ModelForm):
    
    #prochain_appel_date=forms.DateField(widget = forms.SelectDateWidget())
    #prochain_appel_date = forms.DateTimeField(widget=forms.widgets.DateInput(format='%Y/%m/%d %H:%M',attrs={'id': 'datepicker'}))
    #prochain_appel_date = forms.DateTimeField(widget=DateTimePicker(options={'format': '%Y-%m-%d %H:%M','language': 'fr-fr',}),)

    class Meta:

        model = Contact
        fields = ('nom', 'prenom', 'adresse', 'mobile', 'prochain_appel_date')
        widgets = {'prochain_appel_date': forms.DateTimeInput(attrs={'id': 'datetimepicker'})}
        #widgets = {'prochain_appel_date': forms.DateInput(attrs={'id': 'datepicker'})}



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' Username'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': ' Email'}))


    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):

     site_personnel = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':' Site personnel'}))
     #profile_pic = forms.ImageField(widget=forms.TextInput(attrs={'placeholder':' Photo de profil'}))

     class Meta():
         model = UserProfileInfo
         fields = ('site_personnel','profile_pic')




class ProchainappelForm(forms.ModelForm):
    
    class Meta:

        model = Contact
        fields = ('prochain_appel_date',)
        widgets = {'prochain_appel_date': forms.DateTimeInput(attrs={'id': 'datetimepicker'})}
