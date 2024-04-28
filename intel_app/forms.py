from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from . import models


class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control phone-num'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']


class IShareBundleForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control phone', 'placeholder': '0270000000'}))
    offers = forms.ModelChoiceField(queryset=None, to_field_name='price', empty_label=None,
                               widget=forms.Select(attrs={'class': 'form-control airtime-input'}))

    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if status == "User":
            self.fields['offers'].queryset = models.IshareBundlePrice.objects.all()
        elif status == "Agent":
            self.fields['offers'].queryset = models.AgentIshareBundlePrice.objects.all()
        # self.fields['size'].queryset = models.Size.objects.filter(domain=domain)
            

class MTNForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control mtn-phone', 'placeholder': '0200000000'}))
    offers = forms.ModelChoiceField(queryset=models.MTNBundlePrice.objects.all().order_by('price'), to_field_name='price', empty_label=None,
                               widget=forms.Select(attrs={'class': 'form-control mtn-offer'}))


    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if status == "User":
            self.fields['offers'].queryset = models.MTNBundlePrice.objects.all()
        elif status == "Agent":
            self.fields['offers'].queryset = models.AgentMTNBundlePrice.objects.all()
        # self.fields['size'].queryset = models.Size.objects.filter(domain=domain)


class BigTimeBundleForm(forms.Form):
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control phone', 'placeholder': '0270000000'}))
    offers = forms.ModelChoiceField(queryset=models.BigTimeBundlePrice.objects.all().order_by('price'),
                                    to_field_name='price', empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-control airtime-input'}))

    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if status == "User":
            self.fields['offers'].queryset = models.BigTimeBundlePrice.objects.all()
        elif status == "Agent":
            self.fields['offers'].queryset = models.AgentBigTimeBundlePrice.objects.all()
        # self.fields['size'].queryset = models.Size.objects.filter(domain=domain)



class CreditUserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=models.CustomUser.objects.all().order_by('username'), to_field_name='username', empty_label=None,
                                  widget=forms.Select(attrs={'class': 'form-control airtime-input'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'GHS 100'}))


class AFARegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control name'}))
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control phone', 'placeholder': '0240000000'}))
    gh_card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control card', 'placeholder': 'GHA-XXXXXXXXXXX-X'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control occ'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control loc'}))
    ghana_regions = (
        ('Ashanti Region', 'Ashanti Region'),
        ('Brong-Ahafo Region', 'Brong-Ahafo Region'),
        ('Central Region', 'Central Region'),
        ('Eastern Region', 'Eastern Region'),
        ('Greater Accra Region', 'Greater Accra Region'),
        ('Northern Region', 'Northern Region'),
        ('Oti Region', 'Oti Region'),
        ('Upper East Region', 'Upper East Region'),
        ('Upper West Region', 'Upper West Region'),
        ('Volta Region', 'Volta Region'),
        ('Western Region', 'Western Region'),
        ('Ahafo Region', 'Ahafo Region'),
        ('Bono Region', 'Bono Region'),
        ('Bono East Region', 'Bono East Region'),
        ('North East Region', 'North East Region'),
        ('Savannah Region', 'Savannah Region')
    )
    region = forms.CharField(
        label='Select Region',
        widget=forms.Select(choices=ghana_regions, attrs={'class': 'form-control region'})
    )
    date_of_birth = forms.CharField(
        widget=forms.DateInput(attrs={'class': 'form-control birth', 'type': 'date'}))

    class Meta:
        model = models.AFARegistration
        fields = ('name', 'phone_number', 'gh_card_number', 'occupation', 'date_of_birth', 'region', 'location')


class VodaBundleForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control phone', 'placeholder': '0200000000'}))
    offers = forms.ModelChoiceField(queryset=models.VodaBundlePrice.objects.all().order_by('price'), to_field_name='price', empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-control airtime-input'}))

    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if status == "User":
            self.fields['offers'].queryset = models.VodaBundlePrice.objects.all()
        elif status == "Agent":
            self.fields['offers'].queryset = models.AgentVodaBundlePrice.objects.all()

        # self.fields['size'].queryset = models.Size.objects.filter(domain=domain)



